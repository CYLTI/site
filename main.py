from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    facts = ["Привет, это сайт по гравити фолз", "Привет, добро пожаловать"]
    return random.choice(facts)

app.run(debug=True)
