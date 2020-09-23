from flask import Flask, render_template, Markup,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, DateField, SubmitField
from wtforms.validators import InputRequired,Length
import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
class ChangeForm(FlaskForm):
    submitbtn = SubmitField('Change Now')
#    dfedithtml = Markup(dfedit)
#    change_rows=SubmitField('Change Now')

class LoginForm(FlaskForm):
    fname = StringField('Enter Name: ', validators=[InputRequired(), \
                        Length(min=1,max=10,message='Must be atleast one character')])
    place = StringField('Enter Place: ',validators=[InputRequired()])
    animal = RadioField('Enter Animal: ', choices=[('Lion','Lion'),('Eagle','Eagle'),('Shark','Shark')], \
                        validators=[InputRequired("Select atleast one Animal !")])
    movie = StringField('Enter Movie: ', validators=[InputRequired()])
    bday = DateField('Enter DOB: ',format='%Y-%m-%d',validators=[InputRequired()])

@app.route("/add", methods=['GET','POST'])
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
        dfhtml=Markup(df.to_html())
        dfallrows=pd.read_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
                              sep=',', header=None)
        dfallhtml = Markup(dfallrows.to_html())
        return render_template('try_submit.html', \
                               dfhtml=dfhtml,dfall=dfallhtml)
    return render_template('try_form.html', form=form)

@app.route("/", methods=['GET','POST'])
# def html_input(c):
#     return '<input name="{}" value="{{}}" />'.format(c)
def chngform():
    chgform = ChangeForm()
    df = pd.read_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
                     sep=',', header=None)
    dfhtml = Markup(df.to_html())
    # dfhtml=df.style.format({c:html_input(c) for c in df.columns}).render()
    print(dfhtml)
    if chgform.validate_on_submit():

            htmltodf=pd.read_html(dfhtml)
            print(htmltodf)
#            chgform.htmltodf.to_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
#                          mode='w', header=False, index=False)
#             dfallrows = pd.read_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
#                                 sep=',', header=None)
#             dfallhtml = Markup(dfallrows.to_html())
            return render_template('try_submit.html', \
                               dfhtml='', dfall='')
    return render_template('try_change.html', chgform=chgform, dfhtml=dfhtml)


if __name__ == '__main__':
    app.run(debug=False)
