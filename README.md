# flask-demo
##### This is base development framework of flask 

##### Flask == 1.0.2

```python
# 个人自建flask蓝图分模块开发项目

# 1. 项目结构
├─demo1
│   -- __init__.py  # demo1 模块初始化
|   -- views.py     # demo1 视图函数
└─demo2
│   -- __init__.py  # demo2 模块初始化
|   -- views.py     # demo2 视图函数
|_ run.py   # 应用入口文件
|_ tools.py # 自封装的工具函数

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

