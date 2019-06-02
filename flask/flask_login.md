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

#### 为蓝本增加视图保护
```
@admin_bp.before_request
@login_required
def login_protect():
    pass
```
