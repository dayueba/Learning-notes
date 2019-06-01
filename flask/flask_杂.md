
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
