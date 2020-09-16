from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')


@app.route("/", methods=['GET','POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>The username is {}.<br><h1>The password is {}.<br><h5> SUBMITTED !!'.format(form.username.data, form.password.data)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)
