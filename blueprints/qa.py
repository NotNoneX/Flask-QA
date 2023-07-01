# -*- coding: UTF-8 -*-
# @Time: 2023/6/20 13:39
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: qa.py
""" 蓝图文件: 问答相关 """
from flask import Blueprint
from flask import g, redirect, url_for
from flask import render_template
from flask import request

from blueprints.forms import QuestionForm, AnswerForm
from decorators import login_required
from exts import db
from models import QuestionModel, AnswerModel

bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route("/")
def index():
    # 从数据库获取所有问答数据, order_by排序方式为创建时间 倒序
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html", questions=questions)


# 发布问答
@bp.route('/qa/publish', methods=['GET', 'POST'])
@login_required
def publish_qa():
    # if not g.userinfo:
    #     # 如果用户未登录 则直接跳转到登录页面
    #     # 但是若多个页面都需要验证登录与否 则需要写很多次 故不实用
    #     print("qa.py_L27: 用户未登录!")
    #     return redirect(url_for("auth.login"))
    if request.method == 'GET':
        return render_template("question.html")
    else:
        form = QuestionForm(request.form)
        result = form.validate()
        if result:
            title = form.title.data
            content = form.content.data
            # 不能直接写g.userinfo.id 否则报错, 也许是因为模型建立了关系
            author = g.userinfo
            # 写入数据库
            question = QuestionModel(title=title, content=content, author=author)
            db.session.add(question)
            db.session.commit()
            print("qa.py_L39_发布成功!")
            # todo: 跳转到详情页 以下暂用
            return redirect(url_for("qa.qa_detail", qid=question.id))
        else:
            return redirect(url_for("qa.public_qa"))


# 问答详情页
@bp.route("/qa/detail/<int:qid>")
def qa_detail(qid):
    question = QuestionModel.query.get(qid)
    return render_template("detail.html", question=question)


# 发布回复
# @bp.route("/answer/publish", methods=['POST'])
# 上面的方式和这个一样, 但这个只能用POST
@bp.post("/answer/publish")
# 还是得加上强制登录装饰器 未登录用户不允许回复
@login_required
def publish_answer():
    answer_form = AnswerForm(request.form)
    if answer_form.validate():
        # 回复者id 当前用户
        answer_id = g.userinfo.id
        # 内容和被回复的问题id
        content = answer_form.content.data
        question_id = answer_form.question_id.data
        answer = AnswerModel(content=content, answer_id=answer_id, question_id=question_id)
        db.session.add(answer)
        db.session.commit()
        print("qa.py_L77: 回复成功!")
        return redirect(url_for("qa.qa_detail", qid=question_id))
    else:
        # 表单验证失败 则跳转回原问答
        print("qa.py_L73: ", answer_form.errors)
        # 从前端传来的表单中获取问题id
        qid = request.form.get("question_id")
        return redirect(url_for("qa.qa_detail", qid=qid))


# 搜索问答
@bp.route('/search')
def search():
    # 注意: post请求用 request.form获取 / get请求用 request.args获取
    para = request.args.get('q')
    # QuestionModel.title.contains() : contains: 包含
    questions = QuestionModel.query.filter(QuestionModel.title.contains(para)).all()
    if request:
        return render_template("index.html", questions=questions)
    else:
        return redirect(url_for('qa.index'))
