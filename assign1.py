import KNN.KNNHelper
import DataSetAnalysis.DataAnalysisHelper
import os

if __name__ == "__main__":
    absolute_path = os.getcwd()
    knn_path = absolute_path + "/KNN/NumberRecognition.mat"
    water_potability_training = absolute_path + "/DataSetAnalysis/water_potability_training.csv"
    water_potability_testing = absolute_path + "/DataSetAnalysis/water_potability_testing.csv"
    KNN.KNNHelper.execute_knn_for_multiple_k_values(knn_path)
    data_analysis = DataSetAnalysis.DataAnalysisHelper.DataAnalysisHelper()
    data_analysis.dataset_analysis_make_auc_for_measurements(water_potability_training, water_potability_testing)
    data_analysis.dataset_analysis_prediction_scores()
