from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8e4ff88aa69e78bad64534b022cf1b3e'

posts = [
 {
      'author': 'Ralph Baraka',
      'title': 'Blog post 1',
      'content': 'First post content',
      'date_posted': 'April 21, 2020'
 },
 {
     'author': 'Peter Issa',
     'title': 'Blog post 2',
     'content': 'Second post content',
     'date_posted': 'April 22, 2020'
 }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) #passing into our templates
    

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/register")
def register():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

