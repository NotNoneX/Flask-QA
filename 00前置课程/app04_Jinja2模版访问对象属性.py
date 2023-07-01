# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 11:59
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app04_Jinja2模版访问对象属性.py
""" Jinja2 模板访问对象属性"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/')
def hello_world():
    user = User(username='NotNoneX', email='NotNoneX@Gmail.com')
    person = {
        "username": "冰糖",
        "email": "NotNoneX@qq.com"
    }
    return render_template("index.html", user=user, person=person)


@app.route('/blog/<article_id>')
def article(article_id):
    # 将参数传给前面的HTML文件
    # 其中art_id 和 uname都是前面HTML文件中定义的变量 后者为传入的参数
    return render_template("articles.html", art_id=article_id, uname="NotNoneX")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
