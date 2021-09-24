import matplotlib.pyplot as py_plot
from pathlib import Path
from DataSetAnalysis import WaterPotabilityAlgo


class DataAnalysisHelper:
    dataset_analysis = None

    def __init__(self):
        self.dataset_analysis = WaterPotabilityAlgo.WaterPotabilityAlgo()

    def dataset_analysis_make_auc_for_measurements(self, training_dataset_path=None, testing_data_set_path=None):
        if training_dataset_path is not None and testing_data_set_path is not None:
            self.dataset_analysis.load_data(training_dataset_path, testing_data_set_path)
        else:
            self.dataset_analysis.load_data(Path("water_potability_training.csv"), Path("water_potability_testing.csv"))
        self.dataset_analysis.make_auc_curve()

    def dataset_analysis_prediction_scores(self):
        predicted_scores_q3 = []
        k_values = [i for i in range(1, 20)]
        for k_value in k_values:
            self.dataset_analysis.train(k_value)
            score = self.dataset_analysis.test()
            predicted_scores_q3.append(score)

        py_plot.figure(3)
        py_plot.plot(k_values, predicted_scores_q3)
        py_plot.xlabel(" K ")
        py_plot.ylabel("Scores")
        py_plot.title("Plots for Water Potability Analysis")
        py_plot.savefig("knn_q3.png")
        print("Done plotting and Plot image is saved as knn_q3.png")
