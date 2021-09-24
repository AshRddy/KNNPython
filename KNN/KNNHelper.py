import KNN.KNNAlgo
from pathlib import Path
import matplotlib.pyplot as py_plot


#
#   Main method states the entry of the program to interact with teh KNN Classifier.
#
def execute_knn_for_multiple_k_values(path=None):
    try:
        final_path = Path("NumberRecognition.mat")
        if path is not None:
            final_path = Path(path)

        predicted_scores_q1 = []
        k_values = [i for i in range(1, 20)]
        knn = KNN.KNNAlgo.KNNAlgorithm(final_path)
        # knn.show_image()
        # Iterate for different K values and get the error rates
        for k_value in k_values:
            # Stating the value of K and the Values to Predict
            knn.train(k_value, "8", "9")
            score = knn.test("8", "9")
            predicted_scores_q1.append(score)

        # Plot for K and Error Rates :
        py_plot.figure(1)
        py_plot.plot(k_values, predicted_scores_q1)
        py_plot.xlabel(" K ")
        py_plot.ylabel("Predicted Scores")
        py_plot.title("Scores for KNN Algorithms")
        py_plot.savefig("knn_q1.png")
        print("Done forming KNN and Plot image is saved as knn_q1.png")
    except Exception as e:
        print(e)
