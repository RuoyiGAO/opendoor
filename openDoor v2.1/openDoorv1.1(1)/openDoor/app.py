from flask import Flask, render_template
from pymongo import MongoClient
from openDoor.forms import LoginForm, RegisterForm
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
client = MongoClient('mongodb://test:test@localhost', 27017)

db = client.dbmovietalk
app.config.from_pyfile('config.py')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    # 实例化表单对象
    form =LoginForm()
    # 1）是否为post提交表单信息  2）是否通过了验证
    if form.validate_on_submit():
        # 获取表单的内容
        email = form.email.data
        password = form.password.data
        if email == '123@qq.com' and password == '123':
            return '登录成功'
        else:
            return '登录失败'
    else:
        return render_template('login.html', form=form)
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return '获取性别%s'%(form.gender.data)
    else:
        return render_template('register.html', form=form)

    @app.route("/test", methods=['POST', 'GET'])
    def test():
        return "我是测试的"
if __name__ == '__main__':
    app.run()

