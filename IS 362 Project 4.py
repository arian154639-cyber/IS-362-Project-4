import pandas as pd
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split

def dataframe():
    dataframe_1 = pd.read_csv("agaricus-lepiota.data", header=None)
    dataframe_1 = dataframe_1[[0, 5, 4]]
    dataframe_1.columns = ["Edible Status", "Odor", "Bruises"]

    dataframe_1["Edible Status"] = dataframe_1["Edible Status"].map({
        "e": 0,
        "p": 1
    })

    dataframe_1["Odor"] = dataframe_1["Odor"].map({
        "a": 0,
        "l": 1, 
        "c": 2,
        "y": 3,
        "f": 4,
        "m": 5,
        "n": 6,
        "p": 7,
        "s": 8
    })

    dataframe_1["Bruises"] = dataframe_1["Bruises"].map({
        "f": 0,
        "t": 1
    })
    return dataframe_1

KNN_dataframe = dataframe()


X = KNN_dataframe[["Odor"]]
y = KNN_dataframe["Edible Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=100
)

KNN1 = KNeighborsClassifier(n_neighbors=100)

KNN1.fit(X_train, y_train)

print(KNN1.score(X_test, y_test))



X = KNN_dataframe[["Bruises"]]
y = KNN_dataframe["Edible Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=100
)

KNN2 = KNeighborsClassifier(n_neighbors=100)

KNN2.fit(X_train, y_train)

print(KNN2.score(X_test, y_test))