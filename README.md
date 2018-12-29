# Virtual Online Judge

后端基于django开发，前端部分bootstrap

### 运行环境

稳定运行环境 Ubuntu16.04 LTS

### 需要的第三方库及软件

+ Celery 4.2
+ RabbitMQ 4.0
+ BeautifulSoup4
+ requests 2.18

### 安装方法

+ pip install celery
+ pip install celery
+ pip install beautifulsoup4
+ sudo apt install rabbitmq

### 邮箱配置方法

在OJ文件夹下添加private_settings.py文件，添加以下内容

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'your user'
EMAIL_HOST_PASSWORD = 'your password'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'your email address'
PRIVATE_LOCAL_HOST = "the server‘s address"
```

