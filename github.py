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
        response_user = requests.get(base_url + githubname)
        # Retrieve the JSON response for user information
        user_info = response_user.json()

        # Send a GET request to the GitHub API for repository information
        response_repos = requests.get(base_url + githubname + "/repos")
        # Retrieve the JSON response for repository information
        repos_info = response_repos.json()

        # Check if the user is not found
        if "message" in user_info:
            
            # Render the template "index.html" with an error message
            return render_template("index.html", error = "User Not Found.")
        
        else:

            # Render the template "index.html" and pass the user_info and the repos_info to be displayed
            return render_template("index.html", profile = user_info, repos = repos_info)

    else:

        # If the request is GET, render the template "index.html" without any user information
        return render_template("index.html")

if __name__ == "__main__":
    
    # Run the Flask app in debug mode
    app.run(debug=True)