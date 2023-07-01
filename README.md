# 说明文件

## 使用说明

```
# 启动命令
python app.py
```
## 数据库模型使用命令

```bash
# 仅首次
flask db init
# 后续操作
flask db migate
flask db upgrade
```

## 文件说明

- blueprints: 蓝图包
    - [x] auth.py: 认证相关蓝图
    - [x] forms.py: 登录注册认证
    - [x] qa.py: 问答模块蓝图
- static: 静态文件目录
    - [x] js
    - [x] css
    - [x] others
- migrations: 数据库修改记录`自动生成`
- app.py: 入口文件
- config.py: 配置文件
- decorators.py: 自建装饰器
- exts.py: 扩展文件
- models.py: 数据库模型

## 涉及知识

- url传参
- 邮件发送
- ajax
- orm与数据库
- Jinja2模板
- cookie和session原理
- 搜索
