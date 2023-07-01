# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 17:18
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app10_ORM模型与表映射.py
""" ORM对象关系映射 与 表的映射 """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# sql语句需要用此方法包裹 否则报错

app = Flask(__name__)
# 数据库信息
HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "flask"
# 配置flask的SQLAlchemy数据库连接信息
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=UTF8MB4"

# 在app.config中配置好数据库连接信息
# 然后使用SQLAlchemy(app)创建一个db对象
# SQLAlchemy会自动读取app.config中的数据库连接信息
db = SQLAlchemy(app)


class User(db.Model):
    # 定义表 设置表名
    __tablename__ = "user"
    # 分别设置三个列(字段) id, username, password 并且加上字段类型和限制
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar, notnull 字符串 非空
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)


# 插入数据
# user = User(username="法外狂徒张三", password='111111')
# SQL: insert into user(username, password) values("法外狂徒张三", '111111');

# 提交表结构
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
