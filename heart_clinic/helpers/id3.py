# ID3 (Iterative Dichotomiser 3) Algorithm implementation from scratch
# see https://guillermoarriadevoe.com/blog/building-a-id3-decision-tree-classifier-with-python


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score


class GadId3Classifier:
    def __init__(self):
        self.tree = None

    def fit(self, train_input, train_output):
        data = train_input.copy()
        data[train_output.name] = train_output
        self.tree = self.decision_tree(data, data, train_input.columns, train_output.name)

    def predict(self, pred_input):
        # convert input data into a dictionary of samples
        samples = pred_input.to_dict(orient='records')
        predictions = []

        # make a prediction for every sample
        for sample in samples:
            predictions.append(self.make_prediction(sample, self.tree, default='positive'))

        return predictions

    @staticmethod
    def entropy(attribute_column):
        # find unique values and their frequency counts for the given attribute
        values, counts = np.unique(attribute_column, return_counts=True)

        # calculate entropy for each unique value
        entropy_list = []

        for i in range(len(values)):
            probability = counts[i] / np.sum(counts)
            entropy_list.append(-probability * np.log2(probability))

        # calculate sum of individual entropy values
        total_entropy = np.sum(entropy_list)

        return total_entropy

    def information_gain(self, data, feature_attribute_name, target_attribute_name):
        # find total entropy of given subset
        total_entropy = self.entropy(data[target_attribute_name])

        # find unique values and their frequency counts for the attribute to be split
        values, counts = np.unique(data[feature_attribute_name], return_counts=True)

        # calculate weighted entropy of subset
        weighted_entropy_list = []

        for i in range(len(values)):
            subset_probability = counts[i] / np.sum(counts)
            subset_entropy = self.entropy(
                data.where(data[feature_attribute_name] == values[i]).dropna(
                    )[target_attribute_name])
            weighted_entropy_list.append(subset_probability * subset_entropy)

        total_weighted_entropy = np.sum(weighted_entropy_list)

        # calculate information gain
        information_gain = total_entropy - total_weighted_entropy

        return information_gain

    def decision_tree(self, data, original_data, feature_attribute_names, target_attribute_name,
                      parent_node_class=None):
        # base cases:
        # if data is pure, return the majority class of subset
        unique_classes = np.unique(data[target_attribute_name])
        if len(unique_classes) <= 1:
            return unique_classes[0]
        # if subset is empty, ie. no samples, return majority class of original data
        elif len(data) == 0:
            majority_class_index = np.argmax(np.unique(original_data[target_attribute_name],
                                                       return_counts=True)[1])
            return np.unique(original_data[target_attribute_name])[majority_class_index]
        # if data set contains no features to train with, return parent node class
        elif len(feature_attribute_names) == 0:
            return parent_node_class
        # if none of the above are true, construct a branch:
        else:
            # determine parent node class of current branch
            majority_class_index = np.argmax(np.unique(data[target_attribute_name],
                                                       return_counts=True)[1])
            parent_node_class = unique_classes[majority_class_index]

            # determine information gain values for each feature
            # choose feature which best splits the data, ie. highest value
            ig_values = [self.information_gain(data, feature, target_attribute_name) for feature in
                         feature_attribute_names]
            best_feature_index = np.argmax(ig_values)
            best_feature = feature_attribute_names[best_feature_index]

            # create tree structure, empty at first
            tree = {best_feature: {}}

            # remove best feature from available features, it will become the parent node
            feature_attribute_names = [i for i in feature_attribute_names if i != best_feature]

            # create nodes under parent node
            parent_attribute_values = np.unique(data[best_feature])
            for value in parent_attribute_values:
                sub_data = data.where(data[best_feature] == value).dropna()

                # call the algorithm recursively
                subtree = self.decision_tree(sub_data, original_data, feature_attribute_names,
                                             target_attribute_name, parent_node_class)

                # add subtree to original tree
                tree[best_feature][value] = subtree

            return tree

    def make_prediction(self, sample, tree, default=None):
        # map sample data to tree
        for attribute in list(sample.keys()):
            # check if feature exists in tree
            if attribute in list(tree.keys()):
                try:
                    result = tree[attribute][sample[attribute]]
                except:
                    if default is None:
                        return 1
                    return default

                # result = tree[attribute][sample[attribute]]

                # if more attributes exist within result, recursively find best result
                if isinstance(result, dict):
                    return self.make_prediction(sample, result, default='positive')
                else:
                    return result


# calculation function
# -----------------------------------------------------------------------
def calculate(excel_file='heart_disease_male.xls', test_data: pd.DataFrame = None):
    df = pd.read_excel(excel_file)

    # drop arabic titles
    df = df.drop(0)

    # drop rows with missing values, missing = ?
    df = df.replace("?", np.nan)
    df = df.dropna()

    # separate target from predictors
    X = df.drop('disease', axis=1).copy()
    y = df['disease'].copy()
    # feature_names = list(df.keys())[:-1]

    # initialize and fit model
    model = GadId3Classifier()

    # split dataset to two datasets: one for training and the other for evaluating
    if test_data is None:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
        model.fit(X_train, y_train)

        # return accuracy score
        y_pred = model.predict(X_test)

    else:
        model.fit(X, y)
        y_pred = model.predict(test_data)

    return y_pred
