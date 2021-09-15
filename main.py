import KNN.KNNAlgo
from pathlib import Path


def main():
    try:
        knn = KNN.KNNAlgo.KNNAlgorithm(Path("KNN/NumberRecognition.mat"))
        knn.train()
    except Exception as e:
        print(e)


main()
