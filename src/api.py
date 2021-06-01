# pylint: disable=C0301, R0913, R0903
# -*- encoding: utf-8 -*-
"""
@File    :  api.py
@Time    :  2021/05/21 22:03:04
@Author  :  Lewis Lin
@Desc    :  None
"""

__all__ = [
    'PredictCategoryIRIS'
]

import joblib

import cherrypy

from src.checker import IRISParamsChecker


class PredictCategoryIRIS:
    """ API: Predict iris category """
    exposed = True

    def __init__(self, model):
        self.model = joblib.load(model['iris_logistic_reg'])
        self.labels = ['setosa', 'versicolor', 'virginica']


    @cherrypy.tools.json_out()
    def GET(
        self,
        sepal_length: float = None,
        sepal_width: float = None,
        petal_length: float = None,
        petal_width: float = None):
        """[summary]

        Args:
            sepal_length (float, optional): [description]. Defaults to None.
            sepal_width (float, optional): [description]. Defaults to None.
            petal_length (float, optional): [description]. Defaults to None.
            petal_width (float, optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        # check parameters
        checker = IRISParamsChecker(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width
        )
        check_result = checker.check()
        if isinstance(check_result, dict):
            cherrypy.response.status = 400
            return check_result

        # combine features
        features = [[float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]]

        # predict
        try:
            label = self.model.predict(features)
            category = self.labels[label[0]]
            return {
                'success': True,
                'status': 'OK',
                'features' : {
                    'sepal_length': float(sepal_length),
                    'sepal_width': float(sepal_width),
                    'petal_length': float(petal_length),
                    'petal_width': float(petal_width)
                },
                'result': {
                    'label': int(label[0]),
                    'category': category
                }
            }
        except Exception as err:
            cherrypy.response.status = 418
            return {
                'success': False,
                'status': 'Error',
                'error': 'PredictError',
                'message': str(err)
            }


    def OPTIONS(self):
        cherrypy.response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        cherrypy.response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return ''
