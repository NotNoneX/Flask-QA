# -*- coding: UTF-8 -*-
# @Time: 2023/6/20 13:18
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: models.py
""" 模型文件 """
from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # unique=True: 用户名唯一
    uname = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    # unique=True: 邮箱唯一
    email = db.Column(db.String(20), nullable=False, unique=True)
    # 注册时间 default默认值
    join_time = db.Column(db.DateTime, default=datetime.now)


# 邮箱与验证码对应表 用于解决用户注册时 对比邮箱与验证码是否对应
class EmailCodeModel(db.Model):
    __tablename__ = 'email_code'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # unique=True: 邮箱唯一
    email = db.Column(db.String(20), nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False)
    # 是否已经使用
    # used = db.Column(db.Boolean, default=False)


# 发布问答表
class QuestionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 作者: 外键, user.id
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 建立关系, backref: 反向引用
    # 建立反向引用关系后, 可以通过userid获取该用户发布的所有问答
    author = db.relationship(UserModel, backref="questions")


# 回复评论模型
class AnswerModel(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    answer_time = db.Column(db.DateTime, default=datetime.now)

    # 外键: 是属于哪个问答的回复 / 外键: 是谁回复的
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    answer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 关系1: 通过question可以取得所有的回复 但是排序默认为按id顺序 所以需要用回复时间重新倒序排列
    question = db.relationship(QuestionModel, backref=db.backref("answers", order_by=answer_time.desc()))
    # 建立关系 可以获取回复者信息
    answer_people = db.relationship(UserModel, backref="answers")
