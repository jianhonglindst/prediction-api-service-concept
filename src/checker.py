# pylint: disable=C0301, R0913, R0903
# -*- encoding: utf-8 -*-
"""
@File    :  checker.py
@Time    :  2021/05/21 22:06:10
@Author  :  Lewis Lin
@Desc    :  None
"""

__all__ = [
    'ParamsChecker',
    'IRISParamsChecker'
]


from abc import ABCMeta
from abc import abstractmethod

from typing import Dict
from typing import Union


class ParamsChecker(metaclass=ABCMeta):
    """ Parameter Checker Base """

    @abstractmethod
    def check(self) -> Union[str, Dict]:
        """Do check
        """


class IRISParamsChecker(ParamsChecker):
    """ IRIS Parameters Checker """

    def __init__(
        self,
        sepal_length: float = None,
        sepal_width: float = None,
        petal_length: float = None,
        petal_width: float = None):

        self.params = {
            'features': {
                'sepal_length': sepal_length,
                'sepal_width': sepal_width,
                'petal_length': petal_length,
                'petal_width': petal_width
            }
        }
        self.error_infomation = {
            'empty_features': [],
            'not_float_features': [],
            'invalid_boundary_features': []
        }


    @staticmethod
    def make_error_message(error: str, message: str) -> Dict:
        """[summary]

        Args:
            error (str): describe error
            message (str): error reason

        Returns:
            Dict
        """
        return {
            'success': False,
            'status': 'ParamsError',
            'error': error,
            'message': message,
        }


    def is_features_valid(self) -> bool:
        """is features valid?
        1. empty?
        2. float?
        3. limit?

        Returns:
            bool
        """
        features = self.params['features']
        for feature, value in features.items():
            if not value:
                self.error_infomation['empty_features'].append(feature)
                continue

            try:
                value = float(value)
            except ValueError:
                self.error_infomation['not_float_features'].append(feature)
                continue

            if value < 0.0:
                self.error_infomation['invalid_boundary_features'].append(feature)
                continue

        if self.error_infomation['empty_features'] or \
            self.error_infomation['not_float_features'] or \
                self.error_infomation['invalid_boundary_features']:
            return True
        return False


    def check(self) -> Union[str, Dict]:
        if self.is_features_valid():
            return self.make_error_message(
                error='InvalidFeatrueError',
                message='empty: {empty}, not_float: {not_float}, invalid_boundary: {invalid_boundary}.'.format(
                    empty=self.error_infomation['empty_features'],
                    not_float=self.error_infomation['not_float_features'],
                    invalid_boundary=self.error_infomation['invalid_boundary_features']
                )
            )
        return 'pass'
