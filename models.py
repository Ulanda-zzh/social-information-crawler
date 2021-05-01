from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/school_message'

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "/home/lmp/sql/sec.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "111111"

db = SQLAlchemy(app)  # 实例化的数据库



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    phone = db.Column(db.String(32), nullable=False, unique=True)  # 账号
    password = db.Column(db.String(64), nullable=False)  # 密码
    messages = db.relationship("Message", backref="user")  # 修正

'''
class Affair(db.Model):
    __tablename__ = "affair"
    aff_thumbnail = #事件缩略图
    aff_headline = db.Column(db.String(64),nullable=False) #事件标题
    aff_pulisher = db.Column(db.String(64),nullable=False) #事件发出人
    aff_content = #事件内容
    aff_type = #事件类型(homework,preview,project,activity，custom tag）
    aff_pulish_time = #事件发出时间
    aff_deadline = #事件截止时间
    aff_urgency = #事件紧急程度
    aff_estimate_time = #预计完成所需时长
    aff_hide = #是否隐藏

class Memorandum(db.Model):
    __tablename__ = "memorandum"
    createtime = #创建时间
    updatetime = #修改时间

class Date(db.Model):
    __tablename__ = "date"
    aff_deadline = 
    aff_pulish_time = 
    createtime = 
    updatetime = 

'''