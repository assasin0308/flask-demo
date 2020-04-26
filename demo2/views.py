from . import demo2_app
from tools import render_result
from flask import request


# 这里开始你的业务逻辑 以下是测试 视图
@demo2_app.route('/demo2',methods=['GET','POST'])
def demo2():
    if request.method == 'GET':
        return render_result('need post request')
    return render_result('this is demo2 module of demo2 view')