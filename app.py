from flask import Flask, render_template, request, flash, redirect, url_for, session
import config
# 要对数据库进行操作
from models import User, Question, Answer
from exts import db
import flask
# 装饰器使用
from functools import wraps
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
# 对db初始化
db.init_app(app)


# 登录限制装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
            # 这里使用了return是因为视图函数需要返回参数
        else:
            return redirect(url_for('login'))
            # 没有登录则返回登录页面

    return wrapper


# 首页
@app.route('/')
def index():
    content = {
        'questions': Question.query.order_by('-create_time').all()
        # 按创建时间排序,前面加负号表示倒序
        # 'questions':Question.query.all()
    }
    return render_template('index.html', **content)


# 登录页面
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')

        user = User.query.filter(User.telephone == telephone,
                                 User.password == password).first()
        if user:

            session['user_id'] = user.id
            # 设置session
            session.permanent = True
            # True默认为cookies储存31天
            print(user.id)
            return redirect(url_for('index'))
        else:
            return '帐号或密码错误'


# 注册页面
@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            # flash('手机号已被注册')
            # return redirect(url_for('regist'))
            return '手机号已被注册'
        else:
            if password1 != password2:
                # flash("密码不一致")
                # return redirect(url_for('regist'))
                return "密码不一致"
            else:
                user = User(
                    telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                flash("注册成功,跳转到登录页面")
                return redirect(url_for('login'))


# 退出页面
@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    session.pop('user_id')
    # del session('user_id')
    # session.clear()
    # 其它session删除办法
    return redirect(url_for('login'))


# 问答页面
@app.route('/requestion/', methods=['GET', 'POST'])
@login_required
def requestion():
    if request.method == 'GET':
        return render_template('requestion.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        # 对数据库进行绑定

        user_id = session.get('user_id')
        # 从session中获取当前用户id

        user = User.query.filter(User.id == user_id).first()
        question.author = user
        # 有点疑问,这是对数据库中的author进行绑定?
        # 那样的话做成下面这样更容易理解
        # question=Question(title=title,content=content,author_id=user.id)?
        #
        # 补充,这是对relationship定义的author进行赋值:所得到的整个对象,然后关联的外键得到其中的数据
        # 具体由sqlalchemy实现...原理不明



        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


# 评论页面
@app.route('/detail/<question_id>/')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)


# 处理发表评论的视图函数
@app.route('/add_answer/', methods=['POST'])
@login_required
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    answer = Answer(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    answer.author = user

    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question

    print(question)



    db.session.add(answer)
    db.session.commit()

    return redirect(url_for('detail', question_id=question_id))

# 搜索视图函数
@app.route('/search/')
def search():
    q = flask.request.args.get('q')
    questions = Question.query.filter(
        or_(
            Question.title.contains(q),
            Question.content.contains(q)))
    context = {'questions': questions}
    return flask.render_template('index.html', **context)


# 请求上下文,渲染全局的id
@app.context_processor
def my_content_processor():
    user_id = session.get('user_id')
    if user_id:
        #判断是否存在
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}
    #为空时返回空字典


def main():
    app.run()


if __name__ == '__main__':
    main()