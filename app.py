from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Welcome to my exchange app!</p>"


# Відображати перелік валют
@app.route('/currency/<review_coins>/review', methods=['GET', 'POST', 'DELETE', 'PUT'])
def review_coins(review_coins):
    if request.method == 'GET':
        return f'Show coin: {review_coins}'
    elif request.method == 'POST':
        return f'Coin Added: {review_coins}'
    elif request.method == 'DELETE':
        return f'Coin deleted: {review_coins}'
    else:
        return f'Coin updated: {review_coins}'


# Вартість по відношенню до іншої валюти
@app.route('/currency/trade/<coin1>/<coin2>', methods=['GET', 'POST'])
def trade_coins(coin1, coin2):
    if request.method == 'GET':
        return f'Trade value: {coin1}/{coin2}'
    else:
        return f'Trade value: {coin1}/{coin2}'


# Відгуки валюти
@app.route('/currency/commentary/<coin>/<commentary>', methods=['GET', 'POST'])
def coins_commentary(coin, commentary):
    if request.method == 'GET':
        return f'Coin history: {coin} {commentary}'
    else:
        return f'Coin history: {coin} {commentary}'


# Історія курсу
@app.route('/currency/history/<coin>/<history>', methods=['GET', 'POST'])
def coins_history(coin, history):
    if request.method == 'GET':
        return f'Coin history: {coin} {history}'
    else:
        return f'Coin history: {coin} {history}'


# Рейтинг валюти
@app.get("/currency/rating/<coin>/<rating>")
def coin_rating(coin, rating):
    return f'Current coin rating:{coin} {rating}'


# Відображати кількість доступної валюти
@app.get("/currency/available/<coin>/<amount>")
def available_currency(coin, amount):
    return f'Current coin rating:{coin} {amount}'


# Баланс користовача
@app.get("/user/balance/<balance>")
def user(balance):
    return f'Your balance:{balance}'


# Переказ
@app.post("/user/transfer/<transfer>")
def user_transfer(transfer):
    return f'Added new transfer:{transfer}'


# Операція обміну
@app.route("/user/exchange/<from_coin_1>/<to_coin_2>")
def user_exchange(from_coin_1, to_coin_2):
    return f'Open new exchange:{from_coin_1} {to_coin_2}'


# Історія користовача
@app.get("/user/history/<history>")
def user_history(history):
    return f'History:{history}'


if __name__ == '__main__':
    app.run(debug=True)
