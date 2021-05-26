from selenium import webdriver
from page.BasePage import BasePage
from time import sleep
from page.PlateJump_Page import *

#使用的浏览器，暂时只支持谷歌浏览器
#影响初始化，暂时停止使用
browser = webdriver.Chrome()

#执行测试的默认网页，也可在脚本中设置为其他网页
test_url = "http://sohu.com"

#是否发送邮件（0：发送；1：不发送）
send_mail =0

#发送邮件账号账号密码/SMTP服务授权码/host
send_mail_account = "629782424@qq.com"
send_mail_password = "vyfewisdravgbbdj"
host = "smtp.qq.com"

#接收邮件账号账号
receive_main_account = "366535162@qq.com"
#是否开启演示模式，0：不开启，1：开启
demonstration = 1