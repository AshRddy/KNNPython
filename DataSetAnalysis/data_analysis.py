import DataSetAnalysis


def main():
    dataset_analysis = DataSetAnalysis.StrokePredictor()
    dataset_analysis.load_data("water_potability.csv")


main()
