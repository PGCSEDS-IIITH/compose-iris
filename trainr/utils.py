import os
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_wine

# define the class encodings and reverse encodings
classes = {0: "class_0", 1: "class_1", 2: "class_2"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def init_model():
    X,y = load_wine(return_X_y=True)
    clf = GaussianNB()
    clf.fit(X,y)
    pickle.dump(clf, open("models/wine_nb.pkl","wb"))


# function to train and save the model as part of the feedback loop
def train_model(data):
    # load the model
    clf = pickle.load(open("models/wine_nb.pkl", "rb"))

    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.wine_class] for d in data]

    # fit the classifier again based on the new data obtained
    clf.fit(X, y)

    # save the model
    pickle.dump(clf, open("models/wine_nb.pkl", "wb"))
