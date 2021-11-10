#Our very basic wine scoring model!!

#import the required libraries
import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#load the dataset
df = pd.read_csv("src/winequality.csv")

#split the data into the target y and features X
y = df["quality"]
X = df.drop(["quality", "type"], axis=1)

#split the data between train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#define the model using a pipeline
model = Pipeline(steps=[("imputer", SimpleImputer(strategy="mean")), #impute missing values
                        ("scaler", StandardScaler()), #scale all the values
                        ("classifier", RandomForestClassifier())]) #use a RFC for classification
                    
#fot the model with the train set
model.fit(X_train, y_train)

#print out the accuracy of the model for those parameters
print("Accuracy: {:.2f}".format(model.score(X_test, y_test)))

#persist the model using joblib
joblib.dump(model, "model.joblib")