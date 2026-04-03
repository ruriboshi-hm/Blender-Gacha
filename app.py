from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

gacha = [
    {"rarity":"SSR", "name":"将棋盤", "about":"駒、盤、駒台まで全て制作。駒の角度と盛上駒の質感表現にこだわった。", "image":["/static/images/shogi.png"], "weight":3},

    {"rarity":"SR", "name":"麻雀牌", "about":"牌のプラスチック感を意識してマテリアルを調整した。", "image":["/static/images/mahjong.png"], "weight":6},
    {"rarity":"SR", "name":"姿見", "about":"家にある姿見を見ながら作った。画像だと分かりにくいが鏡部分は鏡面反射している。", "image":["/static/images/mirror.png"], "weight":5},
    {"rarity":"SR", "name":"ソファ", "about":"1/50スケールで制作。3Dプリンターで印刷して建築模型に使用している。丁度いい座面の厚みにこだわった。", "image":["/static/images/sofa-print.jpg","/static/images/sofa.png"], "weight":6},

    {"rarity":"R", "name":"カプセル剤", "about":"チュートリアル動画を見ながら制作。カプセル部分と中身の比率調整が難しかった。", "image":["/static/images/medicine.png"], "weight":27},
    {"rarity":"R", "name":"マグカップ", "about":"教材を見ながら制作。内側のマテリアルだけメタリックにして、保温できそうな雰囲気を作った。", "image":["/static/images/cup.png"], "weight":27},
    {"rarity":"R", "name":"ドーナツ", "about":"ドーナツ生地の質感表現が難しかった。チョコのテカテカ感が気に入っている。", "image":["/static/images/doughnut.png"], "weight":26}
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