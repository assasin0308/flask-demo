from . import demo2_app
from tools import render_result


# 这里开始你的业务逻辑 以下是测试 视图
@demo2_app.route('/demo2')
def demo2():
    return render_result('this is demo2 module of demo2 view')