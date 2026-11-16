from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Портал настольных ролевых игр"


@app.route("/campaigns")
def campaign_list():
    return "Список кампаний"


@app.route("/campaigns/<int:campaign_id>")
def campaign_detail(campaign_id):
    return f"Страница кампании № {campaign_id}"


if __name__ == "__main__":
    app.run(debug=True)