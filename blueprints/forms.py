# -*- coding: UTF-8 -*-
# @Time: 2023/6/26 15:18
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: forms.py
""" 认证表单 """
import wtforms
from wtforms.validators import Email, Length, EqualTo
from wtforms.validators import InputRequired
from models import UserModel, EmailCodeModel


# Form: 主要用于验证前端提交的数据是否符合要求
# 注册表单验证验证
class RegisterForm(wtforms.Form):
    """
    注意: 以下字段尽可能和提交的表单字段一致 否则可能会出错
    """
    # 邮箱格式
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    # 验证码长度
    verify = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码格式错误")])
    username = wtforms.StringField(validators=[Length(min=5, max=20, message="用户名格式错误")])
    password1 = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])
    # 重复密码 字段验证: 只要等于password则满足
    password2 = wtforms.StringField(validators=[EqualTo("password1", message="密码输入不一致")])

    # 自定义验证 格式: 方法名以[validate_] 开头后面跟上 [需要验证的表单字段名]
    # 1. 邮箱是否已存在
    def validate_email(self, filed):
        email = filed.data
        eml = UserModel.query.filter_by(email=email).first()
        if eml:
            raise wtforms.ValidationError(message="该邮箱已注册!")

    # 2. 验证码是否正确
    def validate_verify(self, filed):
        verify = filed.data
        email = self.email.data
        # 验证邮箱 验证码是否存在且匹配
        email_model = EmailCodeModel.query.filter_by(email=email, code=verify).first()
        if not email_model:
            raise wtforms.ValidationError(message="验证码不正确")

    # 3. 用户名是否已存在
    def validate_username(self, filed):
        uname = filed.data
        user = UserModel.query.filter_by(uname=uname).first()
        if user:
            raise wtforms.ValidationError(message="用户名已存在!")


# 登录表单验证
class LoginForm(wtforms.Form):
    uname = wtforms.StringField(validators=[Length(min=5, max=20, message="用户名格式错误!")]) or wtforms.StringField(
        validators=[Email(message="邮箱格式错误!")])
    # uname = wtforms.StringField(validators=[Length(min=5, max=20, message="用户名格式错误!")])
    # email = wtforms.StringField(validators=[Email(message="邮箱格式错误!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式不正确!")])


# 发布问答表单验证
class QuestionForm(wtforms.Form):
    # 问答标题 内容 字段验证
    title = wtforms.StringField(validators=[Length(min=2, max=100, message="标题格式错误!")])
    content = wtforms.StringField(validators=[Length(min=2, max=1000, message="内容格式错误!")])


# 回复表单
class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=2, max=1000, message="内容格式错误!")])
    # 问题的id
    question_id = wtforms.IntegerField(validators=[InputRequired(message="问题id不能为空")])
