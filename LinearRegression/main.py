import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.datasets import load_boston
from sklearn import linear_model
import statsmodels.api as sm
import statsmodels.formula.api as smf

if __name__ == '__main__':
    boston = load_boston()
    dataset = pd.DataFrame(boston.data, columns=boston.feature_names)
    dataset['target'] = boston.target

    observations = len(dataset)  # number of records
    variables = dataset.columns[:-1]  # columns except for target
    X = dataset.iloc[:, :-1]        # all data, less target column
    y = dataset['target'].values  # all data in target column
    print(X, y)

    Xc = sm.add_constant(X)  # add column for constant B_0
    print(Xc)

    linear_regression = sm.OLS(y, Xc)
    fitted_model = linear_regression.fit()



