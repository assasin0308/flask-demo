from flask import Blueprint

# 创建 demo1子模块蓝图应用
demo2_app = Blueprint('demo2_app',__name__)

# 加载 demo1 视图函数
from .views import demo2