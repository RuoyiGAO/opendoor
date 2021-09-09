from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class LoginForm(FlaskForm):
    # validators：验证
    email = StringField(label='电子邮箱',
                        validators=[DataRequired(message='邮箱不能为空'),

                                    Email(message='请输入有效的邮箱地址')])

    password = PasswordField(label='密码',
                             validators=[DataRequired(message='密码不能为空')])

    submit = SubmitField(label='登录')
# 注册
class RegisterForm(FlaskForm):
    name = StringField(label='用户名',
                       validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField(label='密码',
                             validators=[DataRequired(),
                                         Length(6, 16, message='密码格式不正确')])
    repassword = PasswordField(label='确认密码',
                               validators=[DataRequired(),
                                           EqualTo('password', message='密码不一致')]) #EqualTo 和哪个字段填的内容一样
    email = StringField(label='邮箱',
                        validators=[DataRequired(),
                                    Email(message='邮箱格式错误')])
    phone = StringField(label='电话号码',
                        validators=[DataRequired(),
                                    #验证电话号码，首位为1，11位，使用正则表达式  \d{10}表示数值出现10次
                                    Regexp(r'1\d{10}', message='电话号码格式错误')])
    # 单选框：SelectField
    gender = SelectField( label='性别',
                          coerce=int, # 填写的信息传入后台的类型
                          choices=[(1, '男'),(2,'女')]  # 下拉列表的选项
     )

    # 下拉多选框：SelectMultipleField
    tech = SelectMultipleField(label='擅长领域',
                               coerce=int,
                               choices=[(1,'python'),(2,'linux'),(3,'java'),(4,'c++')])

    submit = SubmitField(label='注册')