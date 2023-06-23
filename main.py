from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home_Page():
    return "<h1 style='text-align:center'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media1.giphy.com/media/grDFHLDd6Bl9vDCr4Z/giphy.gif?cid=ecf05e47xo70yptbs6fxzmnwrqx29y48" \
           "yk6ayll57cqx8uqd&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=400px style='display:block;margin-left:auto;" \
           "margin-right:auto;'>"


@app.route("/<int:user_num>")
def results(user_num):
    randomNum = random.randint(0, 9)
    print(f"")
    if user_num == randomNum:
        return "<h1 style='text-align:center; color:green'>Got it !</h1>" \
               f"<h3 style='text-align:center'>Number is {user_num}, Random Number is {randomNum}</h3>" \
               "<img src='https://media3.giphy.com/media/kCRYIHAtce9XFEkDjd/giphy.gif?cid=ecf05e47gme9ghbiyendsajs7xtv" \
               "lpywa5nyo9at2gnfyo9x&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=500px " \
               "style='display:block;margin-left:auto;margin-right:auto;'>"
    elif user_num > randomNum:
        return "<h1 style='text-align:center; color:red'>Too High!</h1>" \
               f"<h3 style='text-align:center'>Number is {user_num}, Random Number is {randomNum}</h3>" \
               "<img src='https://media2.giphy.com/media/QWw4hc5gTnJhY0BUI3/giphy.gif?cid=ecf05e47gme9ghbiyendsajs7xtvl" \
               "pywa5nyo9at2gnfyo9x&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=500px " \
               "style='display:block;margin-left:auto;margin-right:auto;'>"
    elif user_num < randomNum:
        return "<h1 style='text-align:center; color:blue'>Too Low!</h1>" \
               f"<h3 style='text-align:center'>Number is {user_num}, Random Number is {randomNum}</h3>" \
               "<img src='https://media1.giphy.com/media/BU6R7enV0nWmGuKGUZ/giphy.gif?cid=ecf05e47gme9ghbiyendsajs7xtvl" \
               "pywa5nyo9at2gnfyo9x&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=500px " \
               "style='display:block;margin-left:auto;margin-right:auto;'>"


if __name__ == "__main__":
    app.run(debug=True)
