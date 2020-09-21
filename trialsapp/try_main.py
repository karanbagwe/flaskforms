from flask import Flask, render_template, Markup
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, DateField, SubmitField
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
class ChangeForm(FlaskForm):
    df = pd.read_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
                     sep=',', header=None)
    dfedit = df.style.format('<input name="df" value="{}" />').render()
    dfedithtml = Markup(dfedit)
#    change_rows=SubmitField('Change Now')

class LoginForm(FlaskForm):
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
        dfhtml=Markup(df.to_html())
        dfallrows=pd.read_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
                              sep=',', header=None)
        dfallhtml = Markup(dfallrows.to_html())
        return render_template('try_submit.html', \
                               dfhtml=dfhtml,dfall=dfallhtml)
    return render_template('try_form.html', form=form)

@app.route("/change", methods=['GET','POST'])
def chngform():
    chgform = ChangeForm()
    if chgform.validate_on_submit():
#        if chgform.change_rows.data:
            htmltodf=pd.read_html(chgform.dfedithtml)[0]
            print(chgform.dfedithtml)
            print(htmltodf)
#            chgform.htmltodf.to_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
#                          mode='w', header=False, index=False)
            dfallrows = pd.read_csv(r"C:\Users\USER\PycharmProjects\Web_Forms_VBB\trialsapp\data_files\data.csv", \
                                sep=',', header=None)
            dfallhtml = Markup(dfallrows.to_html())
            return render_template('try_submit.html', \
                               dfhtml='', dfall=dfallhtml)
    return render_template('try_change.html', chgform=chgform)


if __name__ == '__main__':
    app.run(debug=False)
