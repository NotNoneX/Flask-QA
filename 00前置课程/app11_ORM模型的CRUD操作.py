# -*- coding: UTF-8 -*-
# @Time: 2023/6/19 15:34
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app11_ORM模型的CRUD操作.py
""" ORM模型的CRUD操作 增删改查
CREATE READ UPDATE DELETE
"""
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

db = SQLAlchemy(app)


class User(db.Model):
    # 定义表 设置表名
    __tablename__ = "user"
    # 分别设置三个列(字段) id, username, password 并且加上字段类型和限制
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar, notnull 字符串 非空
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)


# 提交表结构
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/user/add')
def add_user():
    # 创建ORM对象 添加记录
    user = User(username="法外狂徒张三", password='111111')
    # 将记录提交至session中
    db.session.add(user)
    # 将session中的改变同步到数据库
    db.session.commit()
    return "用户创建成功"


@app.route('/user/query')
def query_user():
    # 1. get查找: 根据主键查找
    user = User.query.get(1)
    print(f'方式一: {user.id} {user.username} {user.password}')
    # 2. filter_by查找 常用
    users = User.query.filter_by(username="法外狂徒张三")
    for uinfo in users:
        print("方式二: ", uinfo.id, uinfo.username, uinfo.password)
    return "数据查找成功"


@app.route("/user/update")
def update_user():
    # 取得符合查询条件的第一条数据
    user = User.query.filter_by(username="法外狂徒张三").first()
    user.password = "222222"
    # 这步无需加入session回话 因为上面的查询操作已经在回话里了 所以可以直接提交
    db.session.commit()
    return "数据修改成功"


@app.route("/user/delete")
def delete_user():
    # 获取要删除的数据
    user = User.query.get(1)
    # 从session会话中删除数据
    db.session.delete(user)
    # 提交操作至数据库
    db.session.commit()
    return "用户删除成功"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
