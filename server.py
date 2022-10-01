from flask import Flask, render_template
app = Flask(__name__)

# Landing Page on LocalHost5000
@app.route('/')
def localhost():
    return 'You\'ve reached the localhost:5000 local server ran by Steven Tobias! Type in /table at the end of the address bar to get started!'

# Info Table, rendering list of users
@app.route('/table')
def render_table():
    users = [
    {'first_name' : 'James', 'last_name' : 'Bond', 'full_name' : 'James Bond'},
    {'first_name' : 'Lara', 'last_name' : 'Croft', 'full_name' : 'Lara Croft'},
    {'first_name' : 'Austin', 'last_name' : 'Powers', 'full_name' : 'Austin Powers'},
    {'first_name' : 'John', 'last_name' : 'McClain', 'full_name' : 'McClain'}
]
    return render_template("index.html", users = users)

# End boilerplate from Flask import statement
if __name__=="__main__":
    app.run(debug=True)