from app import app, bcrypt, db
from flask import render_template, flash, redirect, url_for, request
from forms import RegisterForm, LoginForm
from models import User
from flask_login import login_user, login_required, current_user, logout_user

@app.route("/")
def index():
    return render_template("index.html", title="MC")

@app.route("/register", methods=["GET","POST"])
def register():
    # 判斷當前client是否為登入狀態
    # if current_user.is_authenticated:
    #     return redirect(url_for("hello"))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data

        # 生成hash 
        password = bcrypt.generate_password_hash(form.password.data)
        # print(username, password)
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        # 使用flash 返回結果至register.html
        flash("Congrats, registration success!", category="success")
        
        # 返回index
        # 不可使用time.sleep
        # return redirect(url_for("index"))
        # return redirect(url_for("login"))
    return render_template("register.html", form=form)

# @app.route("/login", methods=["GET","POST"])
# def login():
#     # 判斷當前client是否為登入狀態
#     if current_user.is_authenticated:
#         return redirect(url_for("hello"))
    
#     form = LoginForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         remember = form.remember.data

#         # 確認user's pw 是否與 hash相同
#         user = User.query.filter_by(username=username).first()
#         if user and bcrypt.check_password_hash(user.password, password):
#             # user exists and password matched
#             login_user(user, remember=remember)
#             flash("Login success", category="info")

#             # 若url中存在變數"next"
#             # if request.args.get("next"):
#             #     next_page = request.args.get("next")
#             #     return redirect(url_for(next_page))
#             return redirect(url_for("hello", username = user.username))

#         flash("User not exists or password not match", category="danger")
#     return render_template("login.html", form=form)

# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for("login"))

@app.route("/hello")
# @login_required
def hello():
    # if request.args.get("next"):
    #     next_page = request.args.get("next")
    #     return redirect(url_for(next_page))
    return render_template("hello.html", title="MC")