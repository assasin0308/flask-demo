### xzkj_flask_model

##### This is base development framework of flask 

##### Flask == 1.0.2

### 1. introduction

```python
# 个人自建flask蓝图分模块开发项目

# 1. 项目结构
├─demo1
│   -- __init__.py  # demo1 模块初始化
|   -- views.py     # demo1 视图函数
└─demo2
│   -- __init__.py  # demo2 模块初始化
|   -- views.py     # demo2 视图函数
|_ config.py     # 配置文件 可使用app.config.from_object(Config)来配置,也可自行动态配置
|_ db_config.py  # 数据库配置文件,该文件集成MySQL,Redis,MongoDB数据库配置,均以字典形式,可扩充
|_ mongo_conn.py # MongoDB数据库连接操作类,实例化后操作
|_ README.md     # 本文件
|_ mysql_conn.py # MySQL数据库连接操作类,为减少连接损耗,此处使用单例模式进行数据库连接
|_ redis_conn.py # Redis数据库连接操作类,实例化后操作
|_ ssdb_conn.py  # SSDB数据库连接操作类,实例化后操作
|_ test_demo.py  # 针对/demo1/demo1/ 接口的单元测试实例,也可作为其他接口的单元测试
|_ run.py   # 应用入口文件
|_ tools.py # 自封装的工具函数,可自行扩充

# 2. 开发步骤
# 2.1 创建子模块目录
# 2.2 创建 __init__.py 初始化文件并引入蓝图初始化
from flask import Blueprint
# 创建 demo1子模块蓝图应用
demo1_app = Blueprint('demo1_app',__name__)

# 2.3 创建子模块视图函数 views.py
from . import demo1_app
from tools import render_result


# 这里开始你的业务逻辑 以下是测试 视图
@demo1_app.route('/demo1')
def demo1():
    return render_result('this is demo1 module of demo1 view')

# 2.4 在__init__.py中 加载子模块视图函数
from flask import Blueprint

# 创建 demo1子模块蓝图应用
demo1_app = Blueprint('demo1_app',__name__)

# 加载 demo1 视图函数
from .views import demo1

# 2.5 在主应用引入子模块
from flask import Flask,jsonify,make_response
from tools import render_result
# 导入 demo1 子模块
from demo1 import demo1_app
# 导入 demo2 子模块
from demo2 import demo2_app


app = Flask(__name__)


# 注册蓝图 引入子模块
app.register_blueprint(demo1_app,url_prefix='/demo1')
app.register_blueprint(demo2_app,url_prefix='/demo2')



# 测试接口 
@app.route('/')
def index():
    return render_result('flask start success,thank you! copy of xinzhengkeji')


# error handler for 404
@app.errorhandler(404)
def request_not_found(e):
    reback_data = {
        "errcode":404,
        "errmsg":" 404 Your request router is not found!",
        "data": ""
    }
    return  make_response(jsonify(reback_data)),404

# error handler for 405
@app.errorhandler(405)
def method_err(e):
    reback_data = {
        "errcode": 405,
        "errmsg": "405 Method Not Allowed,The method is not allowed for the requested URL! ",
        "data": ""
    }
    return make_response(jsonify(reback_data)), 405

# error handler for 500
@app.errorhandler(500)
def internal_err(e):
    reback_data = {
        "errcode": 500,
        "errmsg": "500 Internal Server Error,Please check your code! ",
        "data": ""
    }
    return make_response(jsonify(reback_data)), 500

# error handler for 502
@app.errorhandler(502)
def internal_err(e):
    reback_data = {
        "errcode": 502,
        "errmsg": "502 Bad Way ",
        "data": ""
    }
    return make_response(jsonify(reback_data)), 502


# error handler for 504
@app.errorhandler(504)
def internal_err(e):
    reback_data = {
        "errcode": 504,
        "errmsg": "504 Gateway Time-out ",
        "data": ""
    }
    return make_response(jsonify(reback_data)), 504


if __name__ == '__main__':
    # print(app.url_map)  # url_map 打印所有路由信息
    app.run(host='0.0.0.0',port=5000,debug=True)

```

### 2. flask-mail

```python
# pip install flask-mail
from flask_mail import Mail,Message
app = Flask(__name__)
# 一次性配置多条
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.sina.com', # smtp电子邮件服务器的主机名或IP地址
    MAIL_PORT = 465, # 电子邮件服务器的端口
    MAIL_USE_TLS= True, #是否启用传输层(TLS,transport layer security)安全协议
    MAIL_USE_SSL=True, # 是否启用安全套接字层(SSL，secure sockets Layer)安全协议
    MAIL_USERNAME =  'assasin@sina.com', # 邮件的用户名
    MAIL_PASSWORD =  '*******', # 邮件的密码或授权码

)
mail = Mail(app)

@app.route('/')
def index():
    # sender 发送方 ; recipients 接收方
    msg = Message("this is a test",sender='assasin@sina.com',recipients=['8392@qq.com'])
    # 邮件内容
    msg.body = "flask is best"
    # 发送
    mail.send(msg)
    print("send success")
    return 'index page '


if __name__ == '__main__':
    app.run('0.0.0.0',port=5001)
```

