import pandas as pd


class StrokePredictor:
    __stroke_predictor_model = None
    __data = None

    def load_data(self, path):
        if path is None:
            print("Please add correct data to add data to the model")
        else:
            self.__data = pd.read_csv(path)
            print(self.__data)
