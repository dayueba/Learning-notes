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

默认发信人由

