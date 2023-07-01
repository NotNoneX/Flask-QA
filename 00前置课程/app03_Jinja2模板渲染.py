# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 11:31
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app03_Jinja2模板渲染.py
""" Jinja2 模板渲染"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/blog/<article_id>')
def article(article_id):
    # 将参数传给前面的HTML文件
    # 其中art_id 和 uname都是前面HTML文件中定义的变量 后者为传入的参数
    return render_template("articles.html", art_id=article_id, uname="NotNoneX")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
