# -*- coding: UTF-8 -*-
# @Time: 2023/6/20 13:39
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: auth.py
""" 蓝图文件: 认证相关 """
import random
import string

from flask import Blueprint, jsonify
# 重定向模块 视图函数转url模块
from flask import redirect, url_for
from flask import render_template
from flask import request
# 存放登录信息 flask中的session是经过加密后储存在cookie中的 所以需要设置加密混淆字符(配置文件)
from flask import session
from flask_mail import Message
# flask密码加密模块 flask密码解密对比模块
from werkzeug.security import generate_password_hash, check_password_hash

# 导入自定义的注册验证类
from blueprints.forms import RegisterForm, LoginForm
from exts import mail, db
from models import EmailCodeModel, UserModel

# 实例化蓝图: 蓝图名字, xxx, 蓝图路由前缀 /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


# 登录页, 因为上面定义了前缀, 所以路由地址为 /auth/login
@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            uname = form.uname.data
            # 数据库中查看用户名或邮箱是否存在
            unm_ext = UserModel.query.filter_by(uname=uname).first()
            eml_ext = UserModel.query.filter_by(email=uname).first()
            user = unm_ext or eml_ext
            if user is None:
                # 空处理
                user = "F"
            if user != "F":
                password = form.password.data
                # 从数据库获取用户名或者邮箱对应加密后的密码进行对比
                unm_psw = UserModel.query.filter_by(uname=uname).first()
                eml_psw = UserModel.query.filter_by(email=uname).first()
                if unm_psw is None:
                    # 空处理
                    unm_psw = "用户输入的不是用户名"
                else:
                    # 如果用户输入的是用户名 则获取用户名对应的加密后的密码 重新赋值
                    unm_psw = unm_psw.password
                if eml_psw is None:
                    # 空处理
                    eml_psw = "用户输入的不是邮箱"
                else:
                    # 如果用户输入的是邮箱, 则获取对应的密码 重新赋值
                    eml_psw = eml_psw.password
                # 加密后的密码为其中之一即可
                password_lock = unm_psw or eml_psw
                # 数据库加密后的密码用`解密方法`解密后 与用户的输入的密码进行对比 产生结果
                result = check_password_hash(pwhash=password_lock, password=password)
                if not result:
                    print("auth.py-L68: ", "密码不正确!")
                    return redirect(url_for("auth.login"))
                else:
                    print("auth.py-L71: ", "登录成功")
                    # 若用户输入的用户名不是uname
                    if UserModel.query.filter_by(uname=uname).first() is None:
                        # 则为邮箱 获取用户id存入session
                        uid = UserModel.query.filter_by(email=uname).first().id
                        session['user_id'] = uid
                    else:
                        # 若用户输入的用户名是uname 则获取id 并存入session
                        uid = UserModel.query.filter_by(uname=uname).first().id
                        session['user_id'] = uid
                    return redirect(url_for("qa.index"))
            else:
                print("auth.py-L83: ", "该用户不存在!")
                return redirect(url_for("auth.login"))
        else:
            print("auth.py-L86: ", form.errors)
            return redirect(url_for("auth.login"))


# 退出登录
@bp.route("/logout")
def logout():
    # 清空session
    session.clear()
    # 返回首页
    return redirect("/")


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证: flask-wtf: wtforms

        # 取得前端提交的表单
        form = RegisterForm(request.form)
        # 调用.validate()方法进行验证
        if form.validate():
            # 验证通过 则注册
            username = form.username.data
            password = form.password1.data
            email = form.email.data
            # 写入用户 注意, 这里的密码是明文密码, 不安全所以用
            # from werkzeug.security import generate_password_hash 加密密码
            password_lock = generate_password_hash(password=password, method="scrypt", salt_length=20)
            print("auth.py_L114: ", username, password, password_lock, end="\n")
            user_join = UserModel(uname=username, password=password_lock, email=email)
            db.session.add(user_join)
            db.session.commit()
            # 注册成功后重定向到登录页
            # 方式一, 用flask下的redirect重定向模块 直接写入链接
            # return redirect("/auth/login")
            # 方式二, 用flask下的url_for模块 写视图函数名
            return redirect(url_for("auth.login"))

        else:
            print("auth.py_L125 ", form.errors)
            return redirect(url_for("auth.register"))


# 验证码接口 如果没指定method参数, 默认为get请求
@bp.route("/verify/email")
def get_email_code():
    # /verify/email/<email>
    # /verify/email?email=xxx.qq.com
    # 取得用户输入的邮箱作为收件邮箱 接收验证码
    email = request.args.get("email")
    # 验证码: 随机数字, 字母, 数字+字母组合
    # 用自带的string库和random库生成随机验证码
    # string.digits是0-9的数字 乘4为了增加取值范围 random.sample用于采样以及确定验证码长度
    sample = string.digits * 4
    verify = random.sample(sample, 4)  # 结果为随机列表[1, 2, 3, 4]
    ver_code = "".join(verify)  # 列表转字符串
    # 邮件消息设置 发送邮件
    msg = Message(subject="冰糖flask项目注册验证码", recipients=[email],
                  body=f"这是一条来自flask的验证码邮件, \n你的验证码是{ver_code}"
                  )
    mail.send(msg)
    # 存储验证码方式: 内存/Redis/数据库
    # 先判断邮箱验证码数据库模型内是否已经存在该邮箱 如果存在则直接更新验证码
    exists = EmailCodeModel.query.filter_by(email=email).first()
    if exists:
        exists.code = ver_code
    else:
        # 如果不存在 则向邮箱验证码数据库模型 传入邮箱与验证码
        email_code = EmailCodeModel(email=email, code=ver_code)
        db.session.add(email_code)
    db.session.commit()
    # 返回接口数据 json格式 {"code": 200 / 400 / 500, "msg": "", "data": ""}
    return jsonify({"code": 200, "msg": "success!", "data": None})


# 邮箱配置测试
@bp.route("/mail/test")
def mail_test():
    # 邮件消息设置 发送邮件
    msg = Message(subject="冰糖flask邮箱测试", recipients=["NotNoneX@Gmail.com"], body="这是一条来自flask的测试邮件")
    mail.send(msg)
    return "邮件发送成功"
