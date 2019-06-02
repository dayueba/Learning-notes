# 数据库

### orm的好处

- 不用手写sql语句, 自动处理查询参数的转义, 避免sql注入
- 为不同的数据库提供统一的接口, 可以方便切换数据库
- 灵活性好, 也支持原生sql语句
- 提升效率


orm把底层的sql数据实体转化成高层的python对象
- 表 -> python类
- 字段 -> 类属性
- 记录 -> 类实例

## flask-sqlalchemy
配置
- SQLALCHEMY_DATABASE_URI
- SQLALCHEMY_TRACK_MODIFICATIONS


```
from flask_sqlalchemy import Sqlalchemy
db = Sqlalchemy(app)
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

# 表名为类名的小写 也可以用__tablename__ = 自己设置表名

```

flask shell
```
from app import db
db.create_all()
db.drop_all()
```
curd
```
from app import db, Note
# create
note = Note(body='123')
db.session.add(note)
db.session.commit()

# query
# <模型类>.query.<过滤方法>.<查询方法>

# update
note = Note.query.first()
note.body = '456'
db.session.commit()

# delete
note = Note.query.first()
db.session.delete(note)
db.session.commit()
```

配置shell上下文
```
# 自动导入db, Note
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Note=Note)

```

## 关系
### 一对多
```
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
```
1. 定义外键 (在多的这边定义)
    ```
    class Post(db.Model):
        author_id = db.Column(db.Integer, db.ForeignKey('author.id))

    ```
2. 定义关系属性 (在一的这边定义)
    ```
    # 返回多个记录 称为集合关系属性
    # 第一个参数为另一个模型的名称 
    # 根据另一侧的外键 反向查询
    posts = db.relationship('Post')
    ```
3. 建立关系
    ```
    # 1. 为外键字段赋值
    # 2. 集合关系属性可以像列表一样操作,使用append
    ```
4. 建立双向关系
    ```
    # 在多的一侧访问少的一册
    # 在多的一侧也创建一个relationship函数

    class Post(db.Model):
        anthor = db.relationship('Author', back_populates='posts')
    ```
5. 使用backref简化关系定义
    ```
    posts = db.relationship('Post', backref='author')

    # 如果需要对另一侧的关系属性设置 使用backref函数 比如
    posts = db.relationship('Post', backref=backref('author', uselist=False))

    # 显示好于隐式 尽量使用back_poplulates定义双向关系
    ```

### 多对一
一对多关系反过来就是多对一, 只是从不同的视角出发<br>
当建立双向关系是, 如果不使用backref, 那么一对多和多对一关系模式在定义上完全相同

### 一对一
一对一关系实际是通过建立双向关系的一对多关系的基础上转化而来的<br>
确保两侧的关系都是标量属性, 都只返回单个值<br>
在关系函数中将uselist设置为False
```
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    post = db.relateionship('Post', uselist=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relateionship('Author')
```

### 多对多
要向表示多对多关系表 除了关系两侧的模型外 还需要创建一个关联表<br>
关联表不存储数据, 只用来存储关系两侧模型的外键对应关系
```
tag_table = db.Table(
    'tag', # 关联表的名称
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id))
)

class Student(db.Model):
    # id
    teachers = db.relationship('Teacher',secondary=tag_table,back_populates='students')

class Teacher(db.Model):
    # id 
    students = db.relationship('Student',
    secondary=tag_table,
    back_populates='teachers')
```

## 更新数据表
```
# pipenv install flask-migrate
from flask_migrate import Migrate

migrate = Migrate(app, db)

# 第一次
flask db init

# 生成迁移脚本
flask db migrate -m 'add xxxx'

# 更行数据库
flask db upgrade

# 回滚迁移
flask db downgrade
```

## 数据库进阶实战
### 级联操作(Cascade) 

操作一个对象时 对相关的对象也执行某些操作

使用post comment模型来演示

cascade的常用配置组合

    - save-update, merge  (默认)
    
    - save-update, merge, delete
    
    - all
    
    - all, delete-orphan

1. save-update

​	如果使用db.session.add(post)时,相关的comment对象也会被添加到session中

2. delete

​	当删除post时, 和post相关的所有comments也会被删除

3. delete-orphan

   基于delete级联, 所以必须和delete一起用 通常设为 all, delete-orphan

   除了删除post时, 和post相关的所有comments也会被删除

   当post和comment解除关系时 也会删除comment对象

   
### 事件监听

listen_for() 装饰器, target表示监听的对象, identitier表示被监听事件的标识符, 比如(set, append..) 

