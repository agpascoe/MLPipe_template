#Here goes trainning, evaluation and saving model
from ..data_AT.data_AT import data_adquisition, data_transformation


class di_f_model():
    def __init__(self) -> None:
        pass

    def fit(self, train_features, train_labels):
        pass

    def evaluate(self, test_features, test_labels):
        pass

    def save(self, FILE_PATH):
        pass


data_features, data_labels = data_adquisition(FILE_PATH=FILE_PATH)
train_features, train_labels, test_features, test_labels = data_transformation(data_features, data_labels, percentage=0.2)

model = di_f_model()
model.fit(train_features=train_features, train_labels=train_labels)
model.evaluate(test_features=test_features, test_labels=test_labels)
model.save(FILE_PATH=FILE_PATH)
