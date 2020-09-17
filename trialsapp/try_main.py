from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    function = RadioField('function', choices=[('insert','ADD'),('update','CHANGE'),('delete','REMOVE')])


@app.route("/", methods=['GET','POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('try_submit.html', \
                               username=form.username.data, password=form.password.data, \
                               function=form.function.data)
#       return '<h1>The username is {}.<br><h1>The password is {}.<br><h5> SUBMITTED !!'.format(form.username.data, form.password.data)
    return render_template('try_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)
