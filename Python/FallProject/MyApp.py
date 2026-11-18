# import the Flask library into this file
from flask import Flask, render_template

# Create a new Flask app named "app"
app = Flask(__name__)

# Create a home page for our flask app (website)
@app.route('/') # The route for the home page
def Index(): # This function is called when the home page is loaded
    return render_template("index.html") # Load the index html template

if __name__ == '__main__':
    app.run(debug = True)