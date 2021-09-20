import matplotlib.pyplot as py_plot
from scipy.io import loadmat
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import zero_one_loss


class KNNAlgorithm:
    __knn_clf = None
    __mat_raw = None

    def __init__(self, path):
        if path is None:
            raise Exception("Path cannot be null or empty")
        else:
            self.path = path
            self.__mat_raw = loadmat(path)

    # show_image is used to display images from the data source graphically !
    def show_image(self):
        if self.__mat_raw is None:
            print("Please add mat file to show image ")
            return

        image_list = list(self.__mat_raw.keys())
        for image in image_list:
            key = str(image)
            print(key)
            if (key.find("Training") != - 1) and (key.find("8") != -1 or key.find("9") != -1):
                individual_image = self.__mat_raw[image]
                print(image)
                for i in range(0, 10):
                    plot = py_plot.imshow(individual_image[:, :, i])
                    py_plot.show()

    # train is to interact with sklearn to build a model
    def train(self, k_value, to_train1, to_train2):
        if self.__mat_raw is None:
            print("Please add mat file to train ")
            return

        self.__knn_clf = KNeighborsClassifier(k_value)

        print("Splitting out samples started ...")
        training_samples, training_labels = self.__get_samples_and_labels(to_train1, to_train2, "Training")
        print("Training Started ...")
        self.__knn_clf.fit(training_samples, training_labels)
        print("Done Training start predicting ...")

    # test is to interactively test the predictions
    def test(self, to_predict1, to_predict2):
        if self.__mat_raw is None or self.__knn_clf is None:
            print("Please train first to test the data set")
            return
        test_samples, test_labels = self.__get_samples_and_labels(to_predict1, to_predict2, "Testing")
        predictions = self.__knn_clf.predict(test_samples)
        return 1 - zero_one_loss(test_labels, predictions)

    def __get_label(self, key, to_predict1, to_predict2):
        return to_predict1 if key.find("8") != -1 else to_predict2

    def __get_samples_and_labels(self, train_test_number1, train_test_number2, string_to_look_for):
        images = list(self.__mat_raw.keys())
        test_samples = []
        test_labels = []
        for image in images:
            key = str(image)
            if (key.find(string_to_look_for) != - 1) and (
                    key.find(train_test_number1) != -1 or key.find(train_test_number2) != -1):
                nx, ny, n_samples = self.__mat_raw[image].shape
                for i in range(0, n_samples):
                    label = self.__get_label(key, train_test_number1, train_test_number2)
                    individual_image = self.__mat_raw[image]
                    test_samples.append((individual_image[:, :, i]).flatten())
                    test_labels.append(label)
        return test_samples, test_labels
