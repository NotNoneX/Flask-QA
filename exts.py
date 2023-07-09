# -*- coding: UTF-8 -*-
# @Time: 2023/6/20 13:17
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: exts.py
""" 扩展文件: 解决循环引用问题"""
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()
