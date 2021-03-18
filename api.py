import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/plants', methods=['GET'])
def home():
    return "<h2 style=\"color: deeppink\">Plants</h2><p style=\"color: #730050\">mini rose, spider plants, mini orchid, aloe vera</p><p style=\"color: teal\">colors</p>"

app.run()