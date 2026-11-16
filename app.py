from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Главная")


@app.route("/campaigns")
def campaigns():
    # Временные данные: позднее заменим запросом к PostgreSQL.
    campaign_data = [
        {"id": 1, "title": "Тень над Вратами", "system_title": "D&D 5e"},
        {"id": 2, "title": "Пепел Аквилы", "system_title": "Wrath&Glory"},
        {"id": 3, "title": "Первые шаги", "system_title": "Pathfinder 2e"},
    ]
    return render_template(
        "campaigns.html", title="Кампании", campaigns=campaign_data
    )


@app.route("/campaigns/<int:campaign_id>")
def campaign_detail(campaign_id):
    return f"Страница кампании № {campaign_id}"


@app.route("/characters")
def my_characters():
    return render_template("characters.html", title="Мои персонажи")


if __name__ == "__main__":
    app.run(debug=True)
