from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
df=pd.DataFrame()

class LoginForm(FlaskForm):
#    username = StringField('username')
#    password = PasswordField('password')
#    function = RadioField('function', choices=[('insert','ADD'),('update','CHANGE'),('delete','REMOVE')])
    fname = StringField('fname')
    place = PasswordField('place')
    animal = RadioField('animal', choices=[('Lion','Lion'),('Eagle','Eagle'),('Shark','Shark')])
    movie = StringField('movie')

@app.route("/", methods=['GET','POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        dfadd = pd.DataFrame({"Name":[form.fname.data],
                              "Place":[form.place.data],
                              "Animal":[form.animal.data],
                              "Movie":[form.movie.data]})
        df.append(dfadd)
        print(df)
#        datafile=open(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.xls","w+")
#        datafile.write(form.username.data)
#        datafile.write(form.password.data)
#        datafile.write(form.function.data)
#        datafile.close()
        return render_template('try_submit.html', \
                               fname=form.fname.data, place=form.place.data, \
                               animal=form.animal.data,movie=form.movie.data)
#       return '<h1>The username is {}.<br><h1>The password is {}.<br><h5> SUBMITTED !!'.format(form.username.data, form.password.data)
    return render_template('try_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)
