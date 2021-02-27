from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
