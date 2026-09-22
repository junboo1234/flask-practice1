from flask import Flask, render_template

app = Flask(__name__)


@app.route("/profile")
def profile_template_render():
    hobbies = ["운동", "게임", "코딩"]
    return render_template("profile.html", habit=hobbies)


@app.route("/")
def name_template_render():
    return render_template("name.html")


@app.route("/greet/<name>")
def greet_template_render(name):
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)