### 起步
pipenv install flask-mail

from flask_mail import Mail

mail = Mail(app)

### 配置
flask-mail通过连接SMTP服务器来发送邮件
所以 第一步 配置smtp服务器

|       配置键        |           说明           | 默认值    |
| :-----------------: | :----------------------: | --------- |
|     MAIL_SERVER     | 用于发送邮件的SMTP服务器 | localhost |
|      MAIL_PORT      |         发信端口         | 25        |
|    MAIL_USE_TLS     |     是否使用STARTTLS     | False     |
|    MAIL_USE_SSL     |     是否使用SSL/TLS      | False     |
|    MAIL_USERNAME    |    发送服务器的用户名    | None      |
|    MAIL_PASSWORD    |      发送服务的密码      | None      |
| MAIL_DEFAULT_SENDER |       默认的发件人       | None      |

对发送邮件进行加密可以避免邮件在发送过程中被第三方截获和篡改. SSL和TLS是两种常用的电子邮件安全协议.STARTTLS是另一种加密方式,它会对不安全的链接进行升级.

- 使用ssl/tls加密
MAIL_USE_SSL = True
MAIL_POTR = 465

- 使用STARTTLS加密
MAIL_USE_TLS = True
MAIL_PORT = 587

- 不加密时
MAIL_PORT = 25(默认)

默认发信人由一个两元素元组组成, 姓名, 邮箱地址
<div>
MAIL_DEFAULT_SENDER = ('your name', 'your_name@example.com')</div>

如果使用的是邮件服务商的提供的SMTP服务器发信时,
发信人的邮箱地址必须和MAIL_USERNAME相同
```
def send_mail(subject, to, body):
    """
    通用发信函数
    :param subject: 主题 
    :param to: 目的邮箱地址
    :param body: 正文
    :return: 
    """
    message = Message(subject, recipients=[to], body=body)
    mail.send(message)
```

## 使用事务邮件服务SendGird
网站 app.sendgrid.com/signup<br>
获得app key 保存到SENDGRID_API_KEY中<br>

```
# 修改配置
MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'apikey'
MAIL_PASSWORD = os.getenv('SENDGRID_API_KEY')
```

使用官方提供的sdk
```
pipenv install sendgrid
```


## 进阶

- 使用模板
    ```
    def send_mail(subject, to, **kwargs):
        """
        发送有模板的邮件
        :param subject: 
        :param to: 
        :param kwargs: 
        :return: 
        """
        message = Message(subject, recipients=[to])
        message.body = render_template('email/hello.txt', **kwargs)
        message.html = render_template('email/hello.html', **kwargs)
        mail.send(message)
    ```
    <p>
        如果使用SendGrid, 可以使用它提供的在线模板功能
    </p>
- 异步发送邮件

    使用异步任务队列处理工具 比如Celery