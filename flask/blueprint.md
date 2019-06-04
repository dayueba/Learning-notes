# 视图

## 用类描述视图

```
from flask.views import View

class UserView(View):
    methods = ['GET', 'POST']

    def __init__(self, template):
        self.template = template
        super(UserView, self).__init__()
    
    def show(self):
        return render_template(self.template)

app.add_url_rule('/', view_func=UserView.as_view('home', template='home.html'))
```

## 方法视图

```
from flask.views import MethodView

class UserView(MethodView):
    def get(self):
        pass
    
    def post(self):
        pass

app.add_url_rule('/user', view_func=UserView.as_view('user'))
```

## 蓝图
```
from flask import Blueprint

user_bp = Blueprint('user', __name__, template_folder='', static_folder='', url_prefix='')

@user_bp 
def index():
    retrun ''

app.register_blueprint(user_bp)
```