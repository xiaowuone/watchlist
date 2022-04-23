from flask import Flask
#import click
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
#from flask import request, url_for, redirect, flash
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
 # 创建用户加载回调函数,接受用户 ID 作为参数
    user = User.query.get(int(user_id))
 # 用 ID 作为 User 模型的主键查询对应的用户
    return user

@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)

from watchlist import views, errors, commands

