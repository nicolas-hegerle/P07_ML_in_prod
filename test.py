# Testing the endpoint of our API

# Import the required libraries
import requests

# The url to which the test request wil be made
url = "https://wine-o-meter-nhe.herokuapp.com/predict"

# Input and request for a single prediction
input_simple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

# Request the API for a simple prediction
res = requests.post(url, json=input_simple)
print("Server response: {}".format(res))
print("Prediction of the model: {}".format(res.json()))


# Input for multiple predictions
input_multiple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
              [5.0, 0.98, 0.32, 18.9, 0.050, 75.0, 122.0, 0.401, 3.1, 0.21, 1.2]]
}

# Request the API for multiple predictions
res = requests.post(url, json=input_multiple)
print("Server response: {}".format(res))
print("Prediction of the model: {}".format(res.json()))