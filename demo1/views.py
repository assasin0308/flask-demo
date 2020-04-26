from . import demo1_app
from tools import render_result


# 这里开始你的业务逻辑 以下是测试 视图
@demo1_app.route('/demo1')
def demo1():
    return render_result('this is demo1 module of demo1 view')