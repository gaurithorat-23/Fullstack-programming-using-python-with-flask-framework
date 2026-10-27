 #Create separate static routes for Employee, Department, and Contact pages

from flask import Flask

app=Flask(__name__)

@app.route('/Employee')
def Employee():
    return"This is employee information"

@app.route('/Department')
def Department():
   return"This is page about Department"

@app.route('/contact')
def contact():
   return"This is a contact page"


if __name__=="__main__":
 app.run(debug=True)