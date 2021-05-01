from flask import Flask,request,json,jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app, supports_credentials=True)


# 引用加密库
import hashlib
# 引用时间库
import datetime
#json 时间转化
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)

from models import app, db, User



# 配置环境
class Config():
    DEBUG = True
app.config.from_object(Config)


# 用户注册
@app.route("/user/register",methods=["POST"])
def register():
    phone = request.json.get("phone")
    password = request.json.get("password")
    user = User(phone=phone, password=password)
    # 加密密码
    password = hashlib.sha1(password.encode()).hexdigest()
    #user = user_fil(username=username,password=password)
    try:
        session.add(user)
        session.commit()
        return jsonify(msg="注册成功")
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify(msg="注册失败")

# 用户登录
@app.route("/user/login",methods=["POST"])
def login():
    phone = request.json.get("phone")
    password = request.json.get("password")
    # 加密密码
    password = hashlib.sha1(password.encode()).hexdigest()
    returnmsg={"status":0,"desc":"登陆成功","id":1,"username":username,"test":json.dumps(result,cls=DateEncoder,ensure_ascii=False)}

    if not all([phone,password]):
        returnmsg["status"] = 1
        returnmsg["desc"] = "请输入账号和密码"

    user = User.query.filter(User.phone == phone).first()
    if user is None or password != user.password:
        returnmsg["status"] = 1
        returnmsg["desc"] = "账号或密码不正确"

    session["user_phone"] = phone
    session["user_id"] = user.id

    returnmsg["id"] = result[0]["id"]
    returnmsg["info"] = result[0]
    return json.dumps(returnmsg,cls=DateEncoder,ensure_ascii=False)

@app.route("/user/session", methods=["GET"])
def check_user_session():
    phone = session.get("user_phone")
    user_id = session.get("user_id")

    if username is not None:
        # 操作逻辑 数据库什么的
        return jsonify(username=username, user_id=user_id)
    else:
        return jsonify(msg="出错了，没登录")


# 用户退出登录
@app.route("/user/logout",methods=["POST"])
def user_logout():
    session.clear()
    return jsonify(msg="成功退出登录!")

#用户注销 DELETE->/session


# 用户增加标签
@app.route("/tag",methods=["POST"])
def add_tag():
    pass
# 用户删除标签
@app.route("/tag",methods=["DELETE"])
def delete_tag():
    pass


# 用户获取备忘录
@app.route("/memorandum",methods=["GET"])
def view_memorandum():
    pass
# 用户新增备忘录
@app.route("/memorandum",methods=["POST"])
def add_memorandum():
    pass
# 用户读取备忘录
@app.route("/memorandum/<id>",methods=["GET"])
def get_memorandum(id):
    pass
# 用户删除备忘录
@app.route("/memorandum/<id>",methods=["DELETE"])
def delete_memorandum(id):
    pass
# 用户修改备忘录
@app.route("/memorandum/<id>",methods=["PUT"])
def update_memorandum(id):
    pass
# 用户查询备忘录
@app.route("/memorandum/history",methods=["POST""GET"])
def inquery_memorandum():
    pass


# 用户编辑备忘录
@app.route("/memorandum",methods=["PUT"])
def change_memorandum():
    pass


# 用户增加日程
@app.route("/schedule",methods=["POST"])
def add_schedule():
    pass
# 用户删除日程
@app.route("/schedule",methods=["DELETE"])
def delete_schedule():
    pass
# 用户查询日程
@app.route("/schedule/history",methods=["GET"])
def inquery_schedule():
    pass



if __name__ == "__main__":
    #app.run(host="10.21.171.197",port=4444)
    app.run(host=localhost)

