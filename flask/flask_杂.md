
pipenv install

pipenv shell

pipenv run python xx.py

pipenv update 'package name'


python-dotenv
    
    FLASK_APP=
    
    FLASK_ENV=

watchdog --dev

flask run --host=0.0.0.0 --post=8000
flask shell
flask routes
自定义命令
```
@app.cli.command
def hello():
    click.echo('hello')

# flask hello
```

使用工厂模式的好处
1. 可以利用环境的上下文来改变应用的初始配置. 修改配置后, 在服务器创建应用时这些修改能立即生效
2. 方便测试, 可以快速测试拥有不用配置的配置对象
3. 可以很容易地使用相同的配置, 生成相同应用的多个实例. (负载均衡时很有用)
