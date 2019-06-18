'''
pipenv
pipenv install  # 创建虚拟环境
pipenv shell #进入虚拟环境
pipenv run python hello.py
pipenv install <package name>
'''

'''
python-dotenv #环境变量 .env敏感信息 .flaskenv
watchdog 监控文件变动
'''

'''
flask shell  代替 python shell
自动导入上下文(环境)
为了正常运行程序 一些操作相关的状态和数据需要被临时保存下来 这些状态和数据被称为上下文
'''




# 查看sql语句
SQLALCHEMY_ECHO = True


# 默认为模型名的小写
__tablename__ = 'user'

'''
    query
    paginate

    user.query.paginate(1, 10)
        .items
        .page
        .pages
        .has_prev, .has_next

    .filter
        from sqlalchemy.sql.expression import not_, or_
    .filter_by
    .order_by
    .limit
    .all
    .first

    update

'''


'''
    relationship // 一
        lazy
            subquery 子查询
            dynamic 动态 关联对象使用时再加载
        backref
        secondary


'''


'''
flask migrate
'''

'''
jinja
服务器渲染 / JavaScript模板动态生成HTML  {% row %} {% endrow %}
    过滤器
        常见的过滤器
        自定义过滤器

    循环
        loop.index
            .index0....
    宏  #组件 复用

    flask特有的
        config
        request 
'''

'''
wtforms
    SECRET_KEY
    校验器
        自定义校验器
    .hidden_tag()
'''

'''
请求钩子
@app.before_request
@app.teardown_request

'''

'''
自定义错误页面
    @app.errorhandler(404)

from flask.views import View
from flask.views import MethodView

app.add_url_rule()
'''



'''
blueprint
    Buleprint(
        name,
        __name__,
        template_folder,
        static_folder,
        url_prefix
    )

    app.register_blueprint()

'''
