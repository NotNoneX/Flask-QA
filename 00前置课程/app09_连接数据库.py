# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 16:40
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app09_连接数据库.py
""" 连接数据库 """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# sql语句需要用此方法包裹 否则报错
from sqlalchemy import text

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

# 测试数据库是否连接成功 注意: 新版本的SQL语句需要用text声明
with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text('select 1'))
        print(rs.fetchone())  # (1,)


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
