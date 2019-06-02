# 使用CSRFProtect实现CSRF保护
CSRFProtect是flask-wtf内置的扩展

```
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
```
### 使用
```
<form>
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
</form>
```

### 自定义错误函数
```
from flask_wtf.csrf import CSRFError

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('400.html'), 400
```