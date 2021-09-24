import pandas as pd
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


class WaterPotabilityAlgo:
    __stroke_predictor_model = None
    __data_training = None
    __data_testing = None
    __data_raw = None
    __knn_clf = None

    def load_data(self, training, testing):
        if training is None or testing is None:
            print("Please add correct data to add data to the model")
        else:
            self.__data_testing = pd.read_csv(testing).dropna()
            self.__data_training = pd.read_csv(training).dropna()
            self.__data_raw = self.__data_training.append(self.__data_testing)

    def make_auc_curve(self):
        auc_curve = {}
        if self.__data_testing is None or self.__data_training is None:
            print("Please load data to make AUC curve")
            return
        potability = np.array(self.__data_raw["Potability"])
        scores = []
        for key in self.__data_raw.keys():
            if key == "Potability":
                continue
            else:
                arr = np.array(self.__data_raw[key])
                score = roc_auc_score(potability, arr)
                scores.append(score)
                auc_curve[score] = key

        scores.sort(reverse=True)
        print("AUC Scores", scores)
        count = 1
        print("Leading Measurements and its feature names")
        print("--Sn-- : --Feature-- : --Score--")
        for score in scores:
            print("| ", count, ".    |", auc_curve[score], "|    ", score, "  |")
            count += 1

    def train(self, k=5):
        self.__knn_clf = KNeighborsClassifier(k)
        training_samples = self.__data_training.copy()
        training_samples.drop("Potability", axis=1, inplace=True)
        training_samples = np.array(training_samples.values)
        training_labels = np.array(self.__data_training["Potability"].values)
        self.__knn_clf.fit(training_samples, training_labels)

    def test(self):
        if self.__knn_clf is None:
            print("Please train first to test..")
            return
        test_samples = self.__data_testing.copy()
        test_samples.drop("Potability", axis=1, inplace=True)
        return self.__knn_clf.score(test_samples, self.__data_testing["Potability"])