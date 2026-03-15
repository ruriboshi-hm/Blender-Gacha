from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

gacha = [
    {"rarity":"SSR", "name":"将棋盤", "about":"説明文", "image":"/static/images/将棋盤.png", "weight":3},

    {"rarity":"SR", "name":"麻雀牌", "about":"説明文", "image":"/static/images/白ポン.png", "weight":9},
    {"rarity":"SR", "name":"姿見", "about":"説明文", "image":"/static/images/鏡.png", "weight":8},

    {"rarity":"R", "name":"カプセル剤", "about":"説明文", "image":"/static/images/medicine.png", "weight":27},
    {"rarity":"R", "name":"マグカップ", "about":"説明文", "image":"/static/images/無題.png", "weight":27},
    {"rarity":"R", "name":"ドーナツ", "about":"説明文", "image":"/static/images/ドーナツ.png", "weight":26}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gacha")
def draw():
    count = int(request.args.get("count"))
    weights = [item["weight"] for item in gacha]
    results = []

    for i in range(count):
        results.append(random.choices(gacha,weights=weights)[0])

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)