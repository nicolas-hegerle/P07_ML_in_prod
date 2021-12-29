import joblib
from flask import Flask, request, json, jsonify, render_template
from werkzeug.exceptions import HTTPException

MODEL_PATH = "models/wine_classif_model.joblib"

app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Return JSON instead of HTML for HTTP errors (which is the basic error
    response with Flask).
    """
    # Start with the correct headers and status code from the error
    response = e.get_response()
    # Replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


class MissingKeyError(HTTPException):
    # We can define our own error for the missing key
    code = 422
    name = "Missing key error"
    description = "JSON content missing key 'input'."


class MissingJSON(HTTPException):
    # We can define our own error for missing JSON
    code = 400
    name = "Missing JSON"
    description = "Missing JSON."

class DataSizeError(HTTPException):
    #Define our own error to check for the data provided
    code = 422
    name = "Data size error"
    description = "Your data has the wrong size for this model. PLease Check your data"

class DataTypeError(HTTPException):
    #Define our own error to check for data format
    code = 422
    name = "Data type error"
    description = "Please provide only int or float type data"



# define a function to make the predictions
def make_prediction(input):
    """
    Returns a prediction with our regression model.
    """
    # Load the model
    classifier = joblib.load(MODEL_PATH)

    # check that all input lists have the correct number of values
    nb_features = classifier.n_features_in_ #number of expected values for predictions
    input_size = [len(x) for x in input] #lists the size of all data lists
    if input_size != [nb_features] * len(input): #compares sizes
        raise DataSizeError()

    # make the predictions with our loaded model
    prediction = [int(i) for i in classifier.predict(input)]

    return prediction


@app.route("/predict", methods=["POST"])
def predict():
    # Check parameters
    if request.json:
        # Get JSON as dictionnary
        json_input = request.get_json()
        if "input" not in json_input:
            # If 'input' is not in our JSON we raise our own error
            raise MissingKeyError()

        input = json_input['input']

        try:
            input = [[float(i) for i in x] for x in input]
        except ValueError:
            raise DataTypeError()

        wine_score = make_prediction(input)

        # Return prediction
        response = {
            "wine_score" : wine_score,
            }
        return jsonify(response), 200

    raise MissingJSON()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = False, host="0.0.0.0")
