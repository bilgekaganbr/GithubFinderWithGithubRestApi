# Import necessary modules and packages
from flask import Flask, render_template, request
import requests

# Define a Flask application
app = Flask(__name__)

# Base URL for GitHub API
base_url = "https://api.github.com/users/"

@app.route("/", methods = ["GET", "POST"])
def index():

    # Check if the request is POST
    if request.method == "POST":

        # Get the GitHub username from the submitted form
        githubname = request.form.get("githubname")

        # Send a GET request to the GitHub API for user information
        response = requests.get(base_url + githubname)

        # Retrieve the JSON response
        user_info = response.json()

        # Render the template and pass the user_info to be displayed
        return render_template("index.html", profile = user_info)

    else:

        # If the request is GET, render the template without any user information
        return render_template("index.html")

if __name__ == "__main__":
    
    # Run the Flask app in debug mode
    app.run(debug=True)