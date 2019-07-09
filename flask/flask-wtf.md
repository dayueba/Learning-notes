# flask-wtf

```
pipenv install flask-wtf
# 需要配置SECRET_KEY

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    pass

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(
            username=self.username.data
        ).first()

        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        if not self.user.validate_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True
```


### 自定义校验器