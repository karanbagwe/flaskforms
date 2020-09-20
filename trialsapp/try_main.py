from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, DateField
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

class LoginForm(FlaskForm):
#    username = StringField('username')
#    password = PasswordField('password')
#    function = RadioField('function', choices=[('insert','ADD'),('update','CHANGE'),('delete','REMOVE')])
    fname = StringField('Enter Name: ')
    place = StringField('Enter Place: ')
    animal = RadioField('Enter Animal: ', choices=[('Lion','Lion'),('Eagle','Eagle'),('Shark','Shark')])
    movie = StringField('Enter Movie: ')
    bday = DateField('Enter DOB: ',format='%Y-%m-%d')

@app.route("/", methods=['GET','POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        if 'df' not in globals():
            df = pd.DataFrame(columns=['Name', 'Place', 'Animal', 'Movie','DOB'])
        df = df.append({"Name":format(form.fname.data),
                        "Place":format(form.place.data),
                        "Animal":format(form.animal.data),
                        "Movie":format(form.movie.data),
                        "DOB":format(form.bday.data)},
                       ignore_index=True)
        df.to_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
                  mode='a',header=False,index=False)
#        datafile=open(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.xls","w+")
#        datafile.write(form.username.data)
#        datafile.write(form.password.data)
#        datafile.write(form.function.data)
#        datafile.close()
        return render_template('try_submit.html', \
                               df=df)
#                               fname=form.fname.data, place=form.place.data, \
#                               animal=form.animal.data,movie=form.movie.data)
#       return '<h1>The username is {}.<br><h1>The password is {}.<br><h5> SUBMITTED !!'.format(form.username.data, form.password.data)
    return render_template('try_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)
