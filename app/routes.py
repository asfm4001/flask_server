from flask import render_template, flash, redirect, url_for, request
from app.forms import RegisterForm, LoginForm, PasswordResetRequestForm, ResetPasswordForm, PostTweetForm
from app.models import User, Post
from flask_login import login_user, login_required, current_user, logout_user
from app import app, bcrypt, db
from app.email import send_reset_password_mail

@app.route("/", methods=["GET","POST"])
@login_required
def index():
    form = PostTweetForm()
    if form.validate_on_submit():
        body = form.text.data
        post = Post(body=body)  # body僅接收str型態
        current_user.posts.append(post)
        db.session.commit()
        flash("You have post a new tweet.", category="success")
    
    n_followers = len(current_user.followers)
    n_followered = len(current_user.followed)

    # default(初始頁碼): 1
    page = request.args.get('page', 1, type=int)
    # 取得所有post, 依時間排序
    # posts = Post.query.order_by(Post.timestramp.desc()).all() #顯示所有在同一頁
        # paginate(page, 
        #   per_page: 每頁item數, 
        #   error_out: 超出預設值報錯
        #   ), 且返回型態更改為object
    posts = Post.query.order_by(Post.timestramp.desc()).paginate(page=page, per_page=2, error_out=False)

    return render_template("index.html", title="MC", form=form, posts=posts, n_followers=n_followers, n_followered=n_followered, page=page, current_url="index")

@app.route("/register", methods=["GET","POST"])
def register():
    # 判斷當前client是否為登入狀態
    if current_user.is_authenticated:
        return redirect(url_for("hello"))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        # 生成hash 
        password = bcrypt.generate_password_hash(form.password.data)
        # print(username, password)
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()

        # 使用flash 返回結果至register.html
        # flash後馬上轉到"login"，導致看不到!!!
        flash("Congrats, registration success!", category="success")
        
        # 返回index
        # 不可使用time.sleep
        # return redirect(url_for("index"))
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET","POST"])
def login():
#     # 判斷當前client是否為登入狀態
    if current_user.is_authenticated:
        return redirect(url_for("hello"))
    
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data

        # 確認user's pw 是否與 hash相同
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # user exists and password matched
            login_user(user, remember=remember)

            # 若url中存在變數"next", 重新導向next
            if request.args.get("next"):
                next_page = request.args.get("next")
                return redirect(next_page)
            return redirect(url_for("hello", username = user.username))

        flash("User not exists or password not match", category="danger")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/hello")
@login_required
def hello():
    if request.args.get("next"):
        next_page = request.args.get("next")
        return redirect(url_for(next_page))
    return render_template("hello.html", title="MC")

# 引入forms.py的PasswordResetRequestForm
@app.route("/send_password_reset_request", methods=["GET", "POST"])
def send_password_reset_request():
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_password_token()

        # email.py
        send_reset_password_mail(user, token)
        flash("Password reset mail is send, please check your mailbox.", category="info")
    return render_template("send_password_reset_request.html", form=form)

# 藉由URL中的token作為輸入參數
@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    # 檢查user是否已登入
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.check_reset_password_token(token)
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash("Your password reset is down, you can login with your new password now", category="info")
            return redirect(url_for("login"))
        else:
            flash("The user is not exist", category="info")
            return redirect(url_for("login"))
    return render_template("reset_password.html", form=form)

@app.route("/user_page/<username>", methods=["GET", "POST"])
def user_page(username):
        user = User.query.filter_by(username=username).first()
        if user:
            page = request.args.get('page', 1, type=int)
            posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestramp.desc()).paginate(page=page, per_page=2, error_out=False)
            # filter_by(Post.user_id = User.id)
            # current_page = "user_page/" + user.username
            return render_template("user_page.html", user=user, posts=posts, page=page)
        else:
            "404"

@app.route("/follow/<username>", methods=["GET", "POST"])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user:
        current_user.follow(user)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestramp.desc()).paginate(page=page, per_page=2, error_out=False)
        return render_template("user_page.html", user=user, posts=posts)
    else:
        "404"

@app.route("/unfollow/<username>", methods=["GET", "POST"])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user:
        current_user.unfollow(user)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestramp.desc()).paginate(page=page, per_page=2, error_out=False)
        return render_template("user_page.html", user=user, posts=posts)
    else:
        "404"