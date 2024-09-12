from flask_wtf import FlaskForm
from wtforms import (
    StringField,    
    PasswordField,
    BooleanField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,   # 資料檢查
    Length, # 長度限制  
    Email,
    EqualTo,
    ValidationError # 偵測相同的username, email
)

# 協助validate_username() 引入User
from models import User

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=8, max=20)])
    # 需安裝email_validator
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    # 檢查username 是否存在DB中
    # 若email也是unique, 需再定義validate_email()
    def validate_username(self, username):  # username 必須與RegisterForm中的變數名相同
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already  token")
    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email already  token")

# 與Register類似
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=8, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    remember = BooleanField("Remember")
    submit = SubmitField("Login")

# 重置password
class PasswordResetRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Send")
    # 檢查email有效性
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        # 假若輸入email不存在
        if not email:
            raise ValidationError("Email not exists.")

# user重設password表格      
class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset Password")