# pylint: disable=C0301, R0913, R0903
# -*- encoding: utf-8 -*-
"""
@File    :  train.py
@Time    :  2021/05/21 22:15:01
@Author  :  Lewis Lin
@Desc    :  None
"""

from typing import List

import joblib

import pandas as pd
from pandas.core.frame import DataFrame

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression


def sklearn_dataset_to_df(dataset) -> DataFrame:
    """convert dataset to df (data.frame)

    Args:
        dataset: sklearn.datasets

    Returns:
        DataFrame
    """
    data_frame = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    data_frame['target'] = pd.Series(dataset.target)
    return data_frame


def convert_dtype_in_df(
    data_frame: DataFrame,
    cols: List,
    dtype: str) -> DataFrame:
    """[summary]

    Args:
        data_frame (DataFrame): DataFrame
        cols (List): columns in data_frame, sub columns in data_frame.
        dtype (str): convert type of cols to dtype.

    Returns:
        DataFrame
    """
    for col in cols:
        data_frame[col] = data_frame[col].astype(dtype)
    return data_frame


def train_iris_model():
    """ training iris model and save model """
    # Get Data: iris
    iris = sklearn_dataset_to_df(dataset=load_iris())

    # Convert column names.
    iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    # Convert feature and response's type
    category_type = ['species']
    iris = convert_dtype_in_df(data_frame=iris, cols=category_type, dtype='category')

    # Shuffle and Split data
    iris_x = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    iris_y = iris.species
    x_train, _, y_train, __ = train_test_split(iris_x, iris_y, test_size=0.1, random_state=0)

    # Logistic Regression
    logistic_reg = LogisticRegression()
    logistic_reg.fit(x_train, y_train)

    # Save model
    joblib.dump(logistic_reg, 'models/iris-logistic-reg.pkl')


if __name__ == '__main__':
    train_iris_model()
