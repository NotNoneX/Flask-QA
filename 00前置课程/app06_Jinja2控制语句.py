# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 15:44
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app06_Jinja2控制语句.py
""" Jinja2 控制语句 """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route("/ctrl")
def ctrl():
    age = 15
    books = [
        {
            "name": "三国演义",
            "author": "罗贯中"
        },
        {
            "name": "西游记",
            "author": "吴承恩"
        },
    ]
    return render_template("ctrl.html", age=age, type=int, books=books)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
