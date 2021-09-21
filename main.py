import KNN.KNNAlgo
from pathlib import Path
import matplotlib.pyplot as p_plot


#
#   Main method states the entry of the program to interact with teh KNN Classifier.
#
def main():
    try:
        predicted_scores = []
        k_values = [i for i in range(1, 20)]
        knn = KNN.KNNAlgo.KNNAlgorithm(Path("KNN/NumberRecognition.mat"))
        # knn.show_image()
        # Iterate for different K values and get the error rates
        for k_value in k_values:
            # Stating the value of K and the Values to Predict
            knn.train(k_value, "8", "9")
            score = knn.test("8", "9")
            predicted_scores.append(score)

        # Prediction Error rates and its corresponding K Values :
        print(predicted_scores)
        print(k_values)

        # Plot for K and Error Rates :
        p_plot.plot(k_values, predicted_scores)
        p_plot.xlabel(" K ")
        p_plot.ylabel("Predicted Scores")
        p_plot.title("Scores for KNN Algorithms")
        p_plot.show()
    except Exception as e:
        print(e)


# Function Invoking !
main()
