# -*- coding: UTF-8 -*-
# @Time: 2023/6/20 13:13
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: config.py
""" 配置文件 """
# 数据库配置
UNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_oa'
DB_URI = f'mysql+pymysql://{UNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI
# 邮箱配置
MAIL_SERVER = "smtp.88.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "NotNoneX@88.com"
MAIL_PASSWORD = "GVgVk4WaKxwaws7I"
MAIL_DEFAULT_SENDER = "冰糖<NotNoneX@88.com>"
# 加密混淆字符 flask中的session是经过加密后储存在cookie中的 所以需要设置加密混淆字符
SECRET_KEY = "NotNoneX"
