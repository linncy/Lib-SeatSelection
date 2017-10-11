#coding= utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField(u'学工号邮箱', validators=[Required(message=u'不能为空'), Length(1, 64),
                                             Email(message=u'不合法的邮箱地址')])
    password = PasswordField(u'密码', validators=[Required(message=u'不能为空')])
    remember_me = BooleanField(u'保持登入')
    submit = SubmitField(u'登入')


class RegistrationForm(FlaskForm):
    email = StringField(u'邮箱（需以.ecnu.edu.cn为后缀）', validators=[Required(message=u'不能为空'), Length(1, 64),
                                           Email(message=u'不合法的邮箱地址'), Regexp('(.*ecnu.edu.cn)', 0,
                                          u'请使用以.ecnu.edu.cn为后缀的邮箱进行认证。')])
    username = StringField(u'姓名', validators=[
        Required(message=u'不能为空'), Length(1, 64)])
    password = PasswordField(u'密码', validators=[
        Required(message=u'不能为空'), EqualTo('password2', message=u'密码不匹配')])
    password2 = PasswordField(u'密码确认', validators=[Required(message=u'不能为空')])
    submit = SubmitField(u'提交认证')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'此邮箱已被注册。')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'此用户名已被使用。')
