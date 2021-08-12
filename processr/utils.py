import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "Iris Setosa", 1: "Iris Versicolour", 2: "Iris Virginica"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "sepal_length": d.sepal_length,
            "sepal_width": d.sepal_length,
            "petal_length": d.petal_length,
            "petal_width": d.petal_width,
            "flower_class": d.flower_class,
        }
        for d in data
    ]

    return processed
