from flask import Blueprint, render_template, request
import requests

views = Blueprint('views', __name__)

@views.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@views.route("/result", methods=["POST"])
def result():
    # 1. get what user typed
    repo_name = request.form.get("repo")

    # 2. call GitHub API
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)

    # 3. check if it worked
    if response.status_code != 200:
        return "Repository not found. Try again."

    # 4. get JSON data
    data = response.json()

    # 5. pick what we want
    repo_data = {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data["language"]
    }

    # 6. send to HTML
    return render_template("result.html", repo=repo_data)