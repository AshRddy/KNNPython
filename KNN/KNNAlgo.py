import matplotlib.pyplot as py_plot
from scipy.io import loadmat
from sklearn.neighbors import KNeighborsClassifier


class KNNAlgorithm:
    __knn_clf = None
    __mat_raw = None

    def __init__(self, path):
        if path is None:
            raise Exception("Path cannot be null or empty")
        else:
            self.path = path
            self.__mat_raw = loadmat(path)

    def show_image(self):
        if self.__mat_raw is None:
            print("Please add mat file to show image ")
            return

        image_list = list(self.__mat_raw.keys())
        for image in image_list:
            key = str(image)
            if key.find("Training") != -1:
                individual_image = self.__mat_raw[image]
                print(image)
                plot = py_plot.imshow(individual_image[:, :, 0])
                py_plot.show()

    def train(self):
        if self.__mat_raw is None:
            print("Please add mat file to train ")
            return

        if self.__knn_clf is None:
            self.__knn_clf = KNeighborsClassifier();

        images = list(self.__mat_raw.keys())
        images_to_train = []
        for image in images:
            key = str(image)
            if key.find("Training") != -1:
                print("Training ... " + key)
                images_to_train.append((self.__mat_raw[image])[:, :, 0])

            self.__knn_clf.fit(images_to_train, key)

        print("Done Training start pridicting ...")

    def test(self):
        if self.__mat_raw is None or self.__knn_clf is None:
            print("Please train first to test ")
            return

        images = list(self.__mat_raw.keys())
        for image in images:
            key = str(image)
            if key.find("Testing") != -1:
                individual_image = (self.__mat_raw[image])[:, :, 0]
                print(self.__knn_clf.predict(individual_image))



