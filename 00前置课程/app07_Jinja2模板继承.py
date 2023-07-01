# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 16:04
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app07_Jinja2模板继承.py
""" Jinja2 模板继承
<!--继承父模板-->
{% extends "base.html" %}

<!--父模板设置占用标签 然后在子模板填写内容-->
{% block body %}
{% endblock %}

"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route("/child1")
def child1():
    return render_template("child1.html")


@app.route("/child2")
def child2():
    return render_template("child2.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
