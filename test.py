# Testing the endpoint of our API

# Import the required libraries
import requests

# The url to which the test request wil be made
url = "https://wine-o-meter-nhe.herokuapp.com/predict"

def request_api(url, json):
    # Request the API for a simple prediction
    res = requests.post(url, json=json)
    print("Server response: {}".format(res))
    print("Prediction of the model: {}".format(res.json()))


# Input for a single prediction
input_simple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

# Input for multiple predictions
input_multiple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
              [5.0, 0.98, 0.32, 18.9, 0.050, 75.0, 122.0, 0.401, 3.1, 0.21, 1.2]]
}

# Input missing value
input_size_error = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

# Input type error
input_type_error = {
    "input": [[7.0, 0.27, 'hello', 20.7, 0.045, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

# Input missing key error
input_missing_key = {
    "thats_my_data": [[7.0, 0.27, 'hello', 20.7, 0.045, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

inputs = [input_simple, input_multiple, input_size_error, input_type_error, input_missing_key]

for input in inputs:
    request_api(url, input)