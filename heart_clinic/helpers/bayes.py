import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class NaiveBayesClassifier:
    """
    Bayes Theorem form
    P(y|X) = P(X|y) * P(y) / P(X)
    """
    def __init__(self):
        self.prior = None
        self.mean = None
        self.var = None
        self.classes = None
        self.count = None
        self.feature_nums = None
        self.rows = None

    def calc_prior(self, features, target):
        """
        prior probability P(y)
        calculate prior probabilities
        """
        self.prior = (features.groupby(target).apply(lambda x: len(x)) / self.rows).to_numpy()

        return self.prior

    def calc_statistics(self, features, target):
        """
        calculate mean, variance for each column and convert to numpy array.
        """
        self.mean = features.groupby(target).apply(np.mean).to_numpy()
        self.var = features.groupby(target).apply(np.var).to_numpy()

        return self.mean, self.var

    def gaussian_density(self, class_idx, x):
        """
        calculate probability from gaussian density function (normally distributed)
        we will assume that probability of specific target value given specific class is normally
        distributed.

        probability density function derived from wikipedia:
        (1/√2pi*σ) * exp((-1/2)*((x-μ)^2)/(2*σ²)), where μ is mean, σ² is variance, σ is quare root
        of variance (standard deviation).
        """

        mean = self.mean[class_idx]
        var = self.var[class_idx]
        print(x.shape, mean.shape, var.shape)
        numerator = np.exp((-1 / 2) * ((x - mean) ** 2) / (2 * var))
        # numerator = np.exp(-((x-mean)**2 / (2 * var)))
        denominator = np.sqrt(2 * np.pi * var)
        prob = numerator / denominator
        return prob

    def calc_posterior(self, x):
        posteriors = []

        # calculate posterior probability for each class
        for i in range(self.count):
            prior = np.log(self.prior[i])  # use the log to make it more numerically stable
            conditional = np.sum(np.log(
                self.gaussian_density(i, x)))  # use the log to make it more numerically stable
            posterior = prior + conditional
            posteriors.append(posterior)
        # return class with highest posterior probability
        return self.classes[np.argmax(posteriors)]

    def fit(self, features, target):
        self.classes = np.unique(target)
        self.count = len(self.classes)
        self.feature_nums = features.shape[1]
        self.rows = features.shape[0]

        self.calc_statistics(features, target)
        self.calc_prior(features, target)

    def predict(self, features):
        preds = [self.calc_posterior(f) for f in features.to_numpy()]
        return preds

    @staticmethod
    def accuracy(y_test, y_pred):
        accuracy = np.sum(y_test == y_pred) / len(y_test)
        return accuracy


def prepare_data(data_frame):
    map_chest_pain_type = {
        'asympt': 0,
        'atyp_angina': 1,
        'typ_angina': 2,
        'non_anginal': 3,
     }
    map_blood_sugar = {
        'FALSE': 0,
        'TRUE': 1,
    }
    map_rest_electro = {
        'normal': 0,
        'left_vent_hyper': 1,
        'st_t_wave_abnormality': 2,
    }
    map_exercice_angina = {
        'no': 0,
        'yes': 1,
    }
    map_disease = {
        'negative': 0,
        'positive': 1,
    }

    data_frame.chest_pain_type = [map_chest_pain_type[item] for item in data_frame.chest_pain_type]
    if not pd.api.types.is_bool_dtype(data_frame.blood_sugar):
        data_frame.blood_sugar = [map_blood_sugar[item] for item in data_frame.blood_sugar]
    data_frame.rest_electro = [map_rest_electro[item] for item in data_frame.rest_electro]
    data_frame.exercice_angina = [map_exercice_angina[item] for item in data_frame.exercice_angina]

    return data_frame


# calculation function
# -----------------------------------------------------------------------
def calculate(excel_file='heart_disease_male.xls', test_data: pd.DataFrame = None):
    df = pd.read_excel(excel_file)

    # drop arabic titles
    df = df.drop(0)

    # drop rows with missing values, missing = ?
    df = df.replace("?", np.nan)
    df = df.dropna()

    df = prepare_data(df)

    # separate target from predictors
    X = df.drop('disease', axis=1).copy()
    y = df['disease'].copy()
    # feature_names = list(df.keys())[:-1]

    # initialize and fit model
    model = NaiveBayesClassifier()

    # split dataset to two datasets: one for training and the other for evaluating
    if test_data is None:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
        model.fit(X_train, y_train)

        # return accuracy score
        y_pred = model.predict(X_test)

    else:
        model.fit(X, y)
        test_data = prepare_data(test_data)
        y_pred = model.predict(test_data)

    return y_pred