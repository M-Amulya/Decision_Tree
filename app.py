from flask import Flask, render_template, request
import pickle


filename = 'final_model.pickle'
app = Flask(__name__, template_folder='template')
loaded_model = pickle.load(open(filename,'rb'))

@app.route("/", methods=["GET"])
def Home_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def prediction_page():
    if request.method == "POST":

        Administrative_Duration = float(request.form["Administrative_Duration"])
        ProductRelated = float(request.form["ProductRelated"])
        ProductRelated_Duration = float(request.form["ProductRelated_Duration"])
        BounceRates = float(request.form["BounceRates"])
        ExitRates = float(request.form["ExitRates"])
        PageValues = float(request.form["PageValues"])


        prediction = loaded_model.predict([[Administrative_Duration, ProductRelated, ProductRelated_Duration, BounceRates, ExitRates, PageValues]])
        return render_template('result.html', result=prediction)

    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
