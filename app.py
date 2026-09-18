from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        user_message = request.form.get("message")

        if name and email and user_message:
            message = "Your message has been received!"
        else:
            message = "Please complete all fields."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)