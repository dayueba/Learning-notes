

## nosql( not only sql)

### 种类

#### 键值数据库
Redis

#### 文档数据库
Mongodb

#### 列式数据库
速度最快

BigTable, Cassandra, HBase

#### 基于图的数据库
Neo4j, InfoGrid

# 在flask中使用nosql

## 配置
```
pipenv install Flask-mongoEngine
from flask_mongoengine import MongoEngine

mongo = MongoEngine(app)

MONGODB_SETTINGS = {
    'db': 'local',
    'host': 'localhost',
    'port': 27017
}
```
## 定义文档
```
class Post(mongo.Document):
    title = mongo.StringField(required=True)
    publish_date = mongo.DateTimeField(
        default=datetime.now()
    )
```

## 字段类型
```
BooleanField
DateTimeField
DictField     能够被json.dumps()序列化的任意python字典
DynamicField  接受任意类型的字段 不会进行类型检查
EmbeddedDocumentField 接收一个被传入的文档, 将其保存在父文档中
FloatField
IntField
ListField  指定类型组成的列表
ObjectIdField
ReferenceField 保存一个文档的唯一id
StringField

如果要实现一对多,可以把一组文档的引用保存在一个列表中,或者把这组文档直接嵌入进去

Field(
    primary_key=None, // 不使用默认生成的唯一标志
    db_field=None,  // 在文档中使用的键名, 默认为那个类属性的名字
    required=False, 
    default=None,
    unique=False,
    unique_with=None, // 可以接收单个字段或者多个字段的列表, 它会确保这些字段的值的组合在每个文档中是唯一的
    choices=None // 如果传入一个列表, 表示只能在这个列表中选择
)
```

## 文档类型

### mongo.Document
只有定义过的键会被保存的数据库中. 其它键会被忽略
### mongo.DynamicDocument
任何额外的键都会被认为时DynamicField, 会被保存到文档中
### mongo.EmbeddedDocument
内嵌文档, 可以保存在别的文档内


## meta属性
```
meta: = {
    'collection': 'user_posts', // 把新写的类绑定到别的集合上
    'max_document': 10000, // 文档的数量
    'max_size': 200000, // 每个文档的大小
    'indexes': [ // 索引
        'title', // 可以是单字段索引
        ('title', 'user') // 也可以是元组指定的多字段索引
    ],
    'ordering': ['-publish_date'], // 排序 -降序 +升序
    'allow_inherintance': True // 允许继承
}
```

## CRUD
### 创建
```
post = Post()
post.title = "Post"
post.text = "text"
post.save()
# 或者
post = Post(title="123", text="asd")

# 如果需要在保存当前对象的同时对引用文档的变更也保存
post.save(cascade=True)

# 跳过类型检查
post.save(validate=False)

```
#### 写入级别
默认情况下, mongodb不会等到已确认的数据写入磁盘才认为写入完成

所以存在它认为写入完成, 但是实际上写入失败的情况

```
# 不会等待写入. 如果发生了错误也不会报告客户端
post.save(write_concern={"w": 0})
# 不会等待写入. 这是缺省行为
post.save(write_concern={"w": 1})
# 会等待写入
post.save(write_concern={"w": 1, "j": True})
```

### 读取
```
Post.objects.all()
Post.objects.limit(5).all()
Post.objects.skip().limit().all() // 跳过前面5个 返回6-10个结果

# 默认情况下, mongodb按照创建时间的顺序返回. 要控制顺序, 可用order_by函数
Post.objects.order_by('+publish_date').all() // 顺序
Post.objects.order_by('-publish_date').all() // 倒序

Post.objects.first()
Post.objects.first_or_404()
Post.objects(id='id值').get()
Post.objects(id='id值').get_or_404()

page = Post.objects.paginate(1, 10) // 分页
page.items()
# 如果文档里有ListField, 则可以用文档对象的paginate_field方法对该列表中的元素进行分页
```
#### 过滤
```
Post.objects(title="post").first()
Post.objects(publish_date__gt=datetime.datetime(2015, 1, 1)).all()
# __gt叫做操作符, 剩下的还有
ne  不等于
lt  小于
lte  大于或等于
gt  大于
gte  大于或等于

# mongoEngine 还提供下面的操作符来检测字符串
exact 字符串相等
iexact 字符串相等(大小写不敏感)
contains 包含
startswith 以该值开始 
endswith 以该值结尾

Post.objects(
    title__not__icontains='post',
    text__istartswith='l',
    publish_date__gt=datetime.datetime(2015, 1, 1)
).order_by('-publish_date').all()

# 直接使用底层的mongo查询
Post.objects(__raw__={'title': 'asd'})
```

### 修改
```
Post.objects(id='id值').update(text='asd')
Post.objects(id='id值').update_one(text='abc')
```
修改键值的其它方式
- set 设置一个值
- unset 删除一个值, 并移除对应的键
- inc 自增
- dec 自减
- push 把一个值加到列表的末尾
- push_all 把几个值加到列表的末尾
- pop 移除列表的第一个或最后一个值
- pull 移除列表中的一个值
- pull_all 移除列表的几个值
- add_to_set 当且仅当某值不在列表中时, 将其添加进列表

### 删除
```
post=Post.objects(id='id值').first()
post.delete()
```
## nosql中的关联关系
### 一对一
#### 第一种方法
使用referenceField指向另一个对象的id
```
class Post(mongo.Document):
    user = mongo.ReferenceField(User)
```
MongoEngine不能一次取到跟某个对象相关联的所有对象

解决办法

> user = User.objects.first()

> Post.objects(user__id=user.id)

#### 第二种方法
在EmbeddedDocumentField中保存EmbeddedDocument
```
class Post(mongo.Document):
    comments = mongo.ListField(mongo.EmbeddedDocumentField(Comment))
```
新增一个评论可以使用append方法
> post.comments.append(comment)

### 多对多
在文档数据库中不存在多对多的概念

处在不同的ListField中的对象, 互相之间没有任何联系. 可以添加一个字符串列表

```
class Post(mongo.Document):
    tags = mongo.ListField( mongo.StringField() )
```
> Post.objects(tags__in="python").all()

> Post.objects(tags__all=["python", "MongoEngine"]).all()

## 例子
#### Post基类
```
class Post(mongo.Document):
    title = mongo.StringField(required)
```

#### 普通博客文章
```
class BlogPost(Post):
    text = db.StringField(required=True)

    @property
    def type(self):
        return "blog"
```

#### 视频文章
```
class VideoPost(Post):
    url = db.StringField(required=True)

    @property
    def type(self):
        return "video"
```

#### 图片文章
```
class ImagePost(Post):
    image_url = db.StringField(required=True)

    @property
    def type(self):
        return "image"
```

#### 引用文章
```
class QuotePost(Post):
    quote = db.StringField(required=True)
    author = db.StringFiel(required=True)

    @property
    def type(self):
        return "quote"
```