# ML in production

## You can check the app @ https://wine-o-meter-nhe.herokuapp.com/
<br>

## Project 🚧

The data-science team has worked together on creating the best model predicting the quality score (from 0 to 10) of multiple wines. The next step is to include this model into the mobile application. The development team is expecting an API endpoint in order to request the model and display the result inside the application.

Your job is to put the trained model into production. Hopefully, the team provided you their work:

- a `model.joblib` which is the trained model pickled (saved using [`joblib`](https://scikit-learn.org/stable/modules/model_persistence.html#python-specific-serialization) library),
- the notebook used to train the model (`Model_Training.ipynb`) and the dataset (`winequality.csv`), so you can have a look,
- a test notebook (`Test_Endpoint.ipynb`) so you can assert that your endpoint is meeting the requirements.

## Goals 🎯

Your mission is to put this model into production by **building an API**. To succeed you need to:

- provide a `/predict` endpoint,
- provide a small documentation for the developer team at the index of your website.

In the following text, we describe the technical expectations:

## **<ins>App URL</ins>**

Try it out, follow the link to learn how to get your predictions:   
https://wine-o-meter-nhe.herokuapp.com/

POST your ```input``` @ https://wine-o-meter-nhe.herokuapp.com/predict to get your predictions



```shell
$ curl -i -H "Content-Type: application/json" -X POST -d '{"input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]}' https://wine-o-meter-nhe.herokuapp.com/predict
```
Or Python:

```python
import requests

response = requests.post("https://wine-o-meter-nhe.herokuapp.com/predict", json={
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
})
print(response.json())
```
