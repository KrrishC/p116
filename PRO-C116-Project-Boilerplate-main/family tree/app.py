# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Krrish" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/1")
def home1():

    name ="Tony"
    age = "40"

    return render_template('father.html', name = name, age = age)
# define the route to mother webpage
@app.route("/2")
def home2():

    name = "Adila"
    age ="40"

    return render_template('mother.html',name = name, age= age)

# define the route to friends webpage
@app.route("/3")
def home3():

    name = "Jack"
    age = "15"

    return render_template('friend.html',name = name , age = age)
# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
