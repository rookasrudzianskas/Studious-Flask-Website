from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

subscribers = []


@app.route('/')
def index():
    title = "Rokas Rudzianskas Portfolio"
    return render_template("index.html", title=title)


@app.route('/about')
def about():
    title = "About Rokas"
    names = ["John", "Rokas", "Marry", "Wes", "Sally"]
    return render_template("about.html", names=names, title=title)


@app.route('/subscribe')
def subscribe():
    title = "Subscribe To My Email Newsletter"
    return render_template("subscribe.html", title=title)


@app.route('/form', methods=["POST"])
def form():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    message = "You have been subscribed to my email newsletter!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("*****@****.***", "******")
    server.sendmail("*****@****.***", email, message)

    if not first_name or not last_name or not email:
        error_statement = "All form fields are required!"
        return  render_template("subscribe.html", error_statement=error_statement, first_name=first_name, last_name=last_name, email=email)

    subscribers.append(f"{first_name} {last_name} | {email}")

    title = "Thank you!"
    return render_template("form.html", title=title, subscribers=subscribers)
