# flask-login

```
pipenv install flask-login

from flask_login import LoginManager

login_manager = LoginManager(app)

# 使用
from flask_login import UserMixin

class User(db.Model, UserMixin):
    pass

```

- is_authenticated 是否登录
- is_active 是否通过了某种激活流程 比如Email认证
- is_anonymous 是否处于未登录的匿名状态
- get_id() 返回User对象的唯一标识 一个Unicode字符串

使用flask_login登录/登出用户只需要在视图函数中调用flask_login提供的login_user()或者logout_user()

login_user()使用flask的session对象将用户的id值存储到用户浏览器的cookie中(名为user_id)  login_user(user, remember)

logout_user()在cookie中删除这个值

#### 记住登录状态 

在login_user()中将remember参数设置为True
这时flask会在cookie中创建名为remember_token

### 获取当前用户
因为session中只会存储登录用户的id, 所以为了让它返回对应的用户对象, 需要一个用户加载函数
```
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user
```

当调用current_user时, 会调用用户加载函数并返回应用对象

如果已经登录则返回User类实例

未登录则返回flask_login内置的AnonymousUserMixin类对象,它的is_authenticated和is_active返回false, is_anonymous返回True

#### 视图保护
from flask_login import login_required

在视图上加@login_required

login_manager.login_view = 'auth.login'

可选
- login_manager.login_message_category = 'warning'
- login_manager.login_message=u'请先登录'
- login_manager.session_protection = 'strong'

#### 为蓝本增加视图保护
```
@admin_bp.before_request
@login_required
def login_protect():
    pass
```

## 用户角色
增加用户权限 则User模型需要跟Role对象建立一个多对多的关联
```
roles = db.Table(
    'role_users',
    db.Column(),
    db.COlumn()
)

class User(db.Model):
    pass

class Role(db.Model):
    pass    

```

### flask-principal
它的机制基于身份(identity)的概念而设计.应用程序中的某些对象,会拥有一种与它相关联的身份

每种身份会关联到need对象, 本质上也就是一些nametuple(具名元祖).Need定义了该身份能做什么事

权限通过need来初始化 定义了对于每种资源来说需要怎样的need对象才可以访问

```
from flask_pricipal import Pricipal, Permission, RoleNeed
principals = Pricoipal(app)
admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))
```

flask-principal需要我们定义一个函数, 当身份改变时,这个函数会把需要添加的need都添加进这个身份对象中
```
from flask_principal import identity_loaded, UserNeed, RoleNeed
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id)

    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))
```

```
from flask_principal import Identity, AnonymousIdentity, identity_changed

# login
identity_changed.send( current_app._get_current_object(), identity=Identity(user.id) )
# logout
identity_changed.send( current_app._get_current_object(), identity=AnonymousIdentity() )
```

```
@poster_permission.require(http_exception=403)

# or

if permission.can() or admin_permission.can():
    pass
```