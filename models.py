from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    # now()获取的是服务器第一次运行的时间
    # now就是每次创建一个模型的时候获取到的当前时间

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 定义外键

    author = db.relationship('User', backref=db.backref('questions'))

    # 定义反转,注意User为函数名,questions应该不是自己的表名,``
    #   对应的应该是上面那个表的关系(所以应该是自定义)

    def __repr__(self):
        return '<Question %r>' % self.title


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # 定义外键
    question_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    # 定义关系
    question = db.relationship('Question',
        backref=db.backref('answers', order_by=create_time.desc()))
    # 定义一个排序后backref=db.backref()
    author = db.relationship('User', backref='answers')

    def __repr__(self):
        return '<Question %r>' % self.question_id