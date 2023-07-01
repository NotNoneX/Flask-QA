# -*- coding: UTF-8 -*-
# @Time: 2023/6/20 13:11
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app.py
""" 项目入口 """
from flask import Flask, session
# flask中的g用于 存储全局变量
from flask import g
import config
from exts import db
from exts import mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定写好的配置文件 config.py
app.config.from_object(config)

# 初始化书籍库 邮箱
db.init_app(app)
mail.init_app(app)

# 数据库迁移三部曲
# 初始化:flask db init
# 生成脚本: flask db migrate
# 提交: flask db upgrade
migrate = Migrate(app=app, db=db)

# 注册蓝图: 问答蓝图, 认证蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


# 钩子函数hook:
# before_first_request:  在第一次请求之前执行 /
# after_request: 请求结束返回响应客户端之前 /
# before_request: 请求进入视图函数之前
# 作用: 每次请求处理之前执行。这个装饰器可以用来实现一些通用的功能，比如请求鉴权、记录请求日志等。
@app.before_request
def my_before_request():
    # 从session中取得用户的uid
    uid = session.get("user_id")
    if uid:
        # 若用户为登录状态 将数据库中的用户信息
        # 通过getattr()方法 存入flask全局模块g中自定义属性user_info
        # setattr(x, y, z)用法: x为需要添加属性的类, y为需要添加的属性名, z为添加的值
        # getattr(x, y)用法: x为需要获取的目标类, y为需要获取的属性名
        user_info = UserModel.query.get(uid)
        setattr(g, "userinfo", user_info)
        print("app.py_L53_当前登录用户: ", g.userinfo.uname)
    else:
        # 若用户未登录则 将g中定义用户信息为空
        setattr(g, "userinfo", None)


# 钩子函数: 上下文处理器
# 作用: 所有自定义变量在所有模板中全局可访问. 函数的返回结果必须是dict
@app.context_processor
def my_context_processor():
    return {"userinfo": g.userinfo}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
