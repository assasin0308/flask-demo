# -*- coding:utf-8 -*-
# @Time: 2020/4/27 16:29
# @Author: assasin
# @Email: assasin0308@sina.com


from flask import jsonify

# return josn data
def render_result(result, errcode = 0, errmsg = 'success'):
    return_data = {
        'errcode': errcode,
        'errmsg': errmsg,
        'data': result
    }
    return jsonify(return_data)

