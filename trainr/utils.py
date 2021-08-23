import os
import pickle
from sklearn.ensemble import RandomForestClassifier

# define the class encodings and reverse encodings
classes = {0: "class_0", 1: "class_1", 2: "class_2"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def init_model():
    if not os.path.isfile("models/wine_rf.pkl"):
        clf = RandomForestClassifier(n_estimators = 30, max_depth=2)
        pickle.dump(clf, open("models/wine_rf.pkl", "wb"))


# function to train and save the model as part of the feedback loop
def train_model(data):
    # load the model
    clf = pickle.load(open("models/wine_rf.pkl", "rb"))

    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.wine_class] for d in data]

    # fit the classifier again based on the new data obtained
    clf.fit(X, y)

    # save the model
    pickle.dump(clf, open("models/wine_rf.pkl", "wb"))
