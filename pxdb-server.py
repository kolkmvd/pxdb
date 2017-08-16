from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/verlof')
def show_verlof():
    return jsonify({"opgenomen" : 200, "uitbetaald" : 100})

@app.route("/vragen")
def show_vragen():
    return jsonify({
            1:
                {"desc":"wie gaat er mee?", "opties" : {1:"ja", 2:"nee"}},
            2:
                {"desc":"zit je haar leuk?", "opties": {1:"ja", 2: "mwah"}}
    })

if __name__ == '__main__':
	app.run()
