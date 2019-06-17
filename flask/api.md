# 用flask编写api

- flask-apispec
- 直接写
- flask-restful

## flask-restful
> pip install flask-restful

```
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
```

### 格式化输出
把任何对象转化为json对象
```
from flask_restful import fields, marshal_with

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')
```

### 参数解析
```
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')
args = parser.parse_args()
```

### 身份认证
#### 认证并返回access令牌
开发者可以发送登录凭证, 得到返回的访问令牌
```
from itsdangerous import TimedJSONWebSignatureSerializer 

s = TimedJSONWebSignatureSerializer(
    current_app.config['secret_key'],
    expiress_in=600   
)

return {"token": s.dumps({'id': user.id})}
```

#### 验证令牌

### 添加cors支持
> pip install flask_cors

```
from flask import Blueprint
from flask_cors import CORS

api_v1 = Blueprint('api_v1', __name__)
CORS(api_v1)
```

#### 参考
https://github.com/greyli/todoism/tree/master/todoism/apis/v1