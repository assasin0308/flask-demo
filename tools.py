from flask import jsonify

# return josn data
def render_result(result, errcode = 0, errmsg = 'success'):
    return_data = {
        'errcode': errcode,
        'errmsg': errmsg,
        'data': result
    }
    return jsonify(return_data)

