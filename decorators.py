# -*- coding: UTF-8 -*-
# @Time: 2023/6/28 17:05
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: decorators.py
""" 装饰器 """
from functools import wraps

from flask import g, redirect, url_for


# 必须登录装饰器
def login_required(func):
    # 保留func的信息
    @wraps(func)
    # 若有函数func(a, b, c), 可以接受abc三个参数
    # 若传入参数 func(1, 2, c=3)
    # 则下面的*args可以代表1, 2, 而**kwargs可以代表c=3
    # 所以, *args和**kwargs同时使用可以代表所有未知参数
    def inner(*args, **kwargs):
        if g.userinfo:

            # 判断用户是否登录, 若有值则为登录状态, 正常执行
            return func(*args, **kwargs)
        else:
            # 无信息, 则未登录, 跳转到登录页面
            print("decorators.py_L26: 请先登录后再进行操作!")
            return redirect(url_for("auth.login"))

    return inner
