# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 16:22
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app08_Jinja2加载静态文件.py
""" Jinja2 加载静态文件 js css
<!--url_for固定写法: url_for('static',filename='资源路径') 写在{{}}内-->

"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route("/static")
def static_demo():
    return render_template("static.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
