import unittest
from run import app
import json

class demo1Test(unittest.TestCase):
    """构造单元测试案例"""

    def setUp(self):
        self.client = app.test_client()


    def test_demo1App_is_success(self):
        """创建进行web请求的客户端 """
        # client = app.test_client()
        # 利用客户端模拟发送请求
        # result = client.post('/demo1/demo1',data={}) # 模拟发送post请求 参数统一封装在 data 字典格式
        result = self.client.get('/demo1/demo1',data={})
        json_data = result.data
        resp = json.loads(json_data)

        # 断言测试
        self.assertIn('errcode',resp)



if __name__ == '__main__':
    unittest.main()