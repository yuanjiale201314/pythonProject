import unittest
import config
from TestRunner import HTMLTestRunner
from TestRunner import SMTP
#定义测试用例的目录为当前目录下的test_case目录
test_dir = './test_case'
test_demonstration_dir = './demonstration'
if config.demonstration == 0:
    suit = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
else:
    suit = unittest.defaultTestLoader.discover(test_demonstration_dir,pattern='test*.py')
if __name__ == '__main__':
    #生成HTML格式的报告
    fp = open('./test_report/result.html','wb')
    runner = HTMLTestRunner(
        stream=fp,
        title = '搜狐网测试报告',
        description = '运行环境：Windows10,Chrome',
    )
    runner.run(suit)
    fp.close()
    # 发邮件功能
    if config.send_mail == 0:
        # smtp = SMTP(user="629782424@qq.com", password="vyfewisdravgbbdj", host="smtp.qq.com")
        # smtp.sender(to="366535162@qq.com", attachments='./test_report/result.html')
        smtp = SMTP(user=config.send_mail_account, password=config.send_mail_password, host="smtp.qq.com")
        smtp.sender(to=config.receive_main_account, attachments='./test_report/result.html')
    # 密码:qwe123456789


