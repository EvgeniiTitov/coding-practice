
class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        if not len(self.ingredients) or not len(self.toppings):
            return []

        out = []
        for ingredient in self.ingredients:
            for topping in self.toppings:
                out.append([ingredient, topping])
        return out

# -----------------------------------------------------------------------------

def unique_names(names1, names2):
    names1_set = set(names1)
    names2_set = set(names2)
    names1_set.update(names2_set)
    return list(names1_set)

# -----------------------------------------------------------------------------

from collections import defaultdict


class RewardPoints:
    BONUS_POINTS = 500

    def __init__(self):
        self.customers = defaultdict(int)

    def earn_points(self, customer_name: str, points: int) -> None:
        if points <= 0:
            return None

        if (
            customer_name not in self.customers
            or self.customers[customer_name] == 0
        ):
            points += RewardPoints.BONUS_POINTS
        self.customers[customer_name] += points

    def spend_points(self, customer_name: str, points: int):
        if points <= 0:
            return None

        # The customer is unknown
        if customer_name not in self.customers:
            return 0

        current_points = self.customers[customer_name]
        if points > current_points:
            return current_points

        self.customers[customer_name] -= points
        return self.customers[customer_name]

# -----------------------------------------------------------------------------

import pandas as pd
import numpy as np

def class_grades(students):
    """
    :param students: (list) Each element of the list is another list with the
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following
      elements: Class name (string), median grade for students in the class (float).
    """
    df = pd.DataFrame(students)
    df.rename(columns={0: "names", 1: "class", 2: "grade"}, inplace=True)
    df = df.groupby("class").median().reset_index(level=0)

    out = []
    for index, row in df.iterrows():
        out.append([row[0], row[1]])

    return out


# -----------------------------------------------------------------------------

def avg_percentage(game_id, ft_number, team, result):
    """
    :param game_id: (list) The ID of the game.
    :param ft_number: (list) The number of the free throw.
    :param team: (list) Which team took the free throw.
    :param result: (list) The result of the free throw, which is either missed or made.
    :returns: (float) The mean value of the percentages (0.0-100.0) of free throws that
               each team scored in each game.
    """
    rows = []
    for game_id_i, ft_number_i, team_i, result_i in zip(
        game_id, ft_number, team, result
    ):
        rows.append([game_id_i, ft_number_i, team_i, result_i])

    df = pd.DataFrame(rows)
    df.rename(
        columns={0: "game_id", 1: "ft_number", 2: "team", 3: "result"},
        inplace=True
    )
    df.replace({"made": 1, "missed": 0}, inplace=True)

    df = df.groupby(["team", "game_id"]).mean()
    print(df)


# -----------------------------------------------------------------------------

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree


def train_and_predict(train_input_features, train_outputs, prediction_features):
    """
    :param train_input_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :param train_outputs: (numpy.array) A one-dimensional NumPy array where each element
                        is a number representing the species of iris which is described in
                        the same row of train_input_features. 0 represents Iris setosa,
                        1 represents Iris versicolor, and 2 represents Iris virginica.
    :param prediction_features: (numpy.array) A two-dimensional NumPy array where each element
                        is an array that contains: sepal length, sepal width, petal length, and petal width
    :returns: (list) The function should return an iterable (like list or numpy.ndarray) of the predicted
                        iris species, one for each item in prediction_features
    """
    model = tree.DecisionTreeClassifier()
    print("Model initialized")

    model.fit(train_input_features, train_outputs)
    print("Model trained")

    predictions = model.predict(prediction_features)

    for prediction_feature, prediction in zip(prediction_features, predictions):
        print(f"Input features {prediction_feature}; Prediction: {prediction}")

    return predictions


if __name__ == "__main__":
    # machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    # print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

    # names1 = ["Ava", "Emma", "Olivia"]
    # names2 = ["Olivia", "Sophia", "Emma"]
    # print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia

    # rewardPoints = RewardPoints()
    # rewardPoints.earn_points('John', 520)
    # print(rewardPoints.spend_points('John', 200))

    # students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4],
    #             ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
    # print(class_grades(students))

    # print(avg_percentage(
    #     [1, 1, 1, 1, 2, 2],
    #     [1, 2, 3, 4, 1, 2],
    #     ['home', 'home', 'away', 'home', 'away', 'home'],
    #     ['made', 'missed', 'made', 'missed', 'missed', 'made']
    # ))

    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=0
    )
    y_pred = train_and_predict(X_train, y_train, X_test)
    if y_pred is not None:
        print(metrics.accuracy_score(y_test, y_pred))
