from flask import Flask,jsonify,make_response,current_app
from tools import render_result
# 导入 demo1 子模块
from demo1 import demo1_app
# 导入 demo2 子模块
from demo2 import demo2_app
# 导入配置文件
# from config import Config


app = Flask(__name__)
# app.config.from_object(Config)

# 注册蓝图 引入子模块
app.register_blueprint(demo1_app,url_prefix='/demo1')
app.register_blueprint(demo2_app,url_prefix='/demo2')



# 测试接口 
@app.route('/')
def index():
    return render_result('flask start success,thank you!')


# error handler for 404
@app.errorhandler(404)
def request_not_found(e):
    resp_data = {
        "errcode":404,
        "errmsg":" 404 Your request router is not found!",
        "data": ""
    }
    return  make_response(jsonify(resp_data)),404

# error handler for 405
@app.errorhandler(405)
def method_err(e):
    resp_data = {
        "errcode": 405,
        "errmsg": " 405 Method Not Allowed,The method is not allowed for the requested URL! ",
        "data": ""
    }
    return make_response(jsonify(resp_data)), 405

# error handler for 500
@app.errorhandler(500)
def internal_err(e):
    resp_data = {
        "errcode": 500,
        "errmsg": "500 Internal Server Error,Please check your code! ",
        "data": ""
    }
    return make_response(jsonify(resp_data)), 500

# error handler for 502
@app.errorhandler(502)
def internal_err(e):
    resp_data = {
        "errcode": 502,
        "errmsg": "502 Bad Way ",
        "data": ""
    }
    return make_response(jsonify(resp_data)), 502


# error handler for 504
@app.errorhandler(504)
def internal_err(e):
    resp_data = {
        "errcode": 504,
        "errmsg": "504 Gateway Time-out ",
        "data": ""
    }
    return make_response(jsonify(resp_data)), 504


if __name__ == '__main__':
    print(app.url_map)  # url_map 打印所有路由信息
    app.run(host='0.0.0.0',port=5000,debug=True)
