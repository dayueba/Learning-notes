# Flask-Assets
下载页面所需要的css和js文件时, 会发送大量http请求, 这造成了web应用的另一个速度瓶颈

浏览器只有在页面html已经加载和解析完成后, 才会开始下载这些额外的文件

服务端可以把依赖的Javascript文件拼接成一个大文件, 把css拼接成另一个. 去除空白字符和空行, 这样可以减少大量时间成本, 可以让文件的体积减少接近30%

另一种方法, 使用特定的http响应头. 告诉浏览器在本地缓存这些文件, 只需要在文件改变时重新下载

## 安装和配置

> pipenv install Flask_assets cssmin jsmin

某些只有的特定页面才需要的文件没必要打包

```
from flask_assets import Environment, Bundle

assets_env = Enviroment(app)

css_all = Bundle(
    'css/bootstrap.css',
    filters='cssmin',
    output='css/common.css'
)

js_all = Bundle(
    'js/bootstrap.js',
    'js/jquery.js',
    filters='jsmin',
    output='js/common.js'
)

assets_env.register('css_all', css_all)
assets_env.register('js_all', js_all)

class DevConfig(Config):
    ASSETS_DEBUG = True // 不要在开发环境中编译
```

## 生成资源集文件
flask assets build

## 模板中使用
```
<link href='css/bootstrap.css'>
# 修改为
{% assets "css_all" %}
<link href="{{ ASSET_URL }}">
{% endassets %}

# js同理
```

## 反思
思想就像是制作雪碧图 以及 webpack打包