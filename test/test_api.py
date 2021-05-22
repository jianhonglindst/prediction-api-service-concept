# pylint: disable=C0301, R0913, R0903
# -*- encoding: utf-8 -*-
"""
@File    :  test_api.py
@Time    :  2021/05/21 22:06:34
@Author  :  Lewis Lin
@Desc    :  None
"""

import json

from requests import request


def test_predict_category_iris_status_ok():
    url = 'http://localhost:8080/predict/category/iris'

    # GET
    # STATUS: OK
    params = {'sepal_length': 5.1, 'sepal_width': 3.4, 'petal_length': 7.5, 'petal_width': 2.1}
    answer = {'success': True, 'status': 'OK'}

    response = request(method='GET', url=url, params=params)
    return_body = json.loads(response.text)

    assert response.status_code == 200
    assert return_body['success'] == answer['success']
    assert return_body['status'] == answer['status']


def test_predict_category_iris_status_params_error():
    url = 'http://localhost:8080/predict/category/iris'

    # GET
    # STATUS: ParamsError
    params = {'sepal_length': 'string', 'sepal_width': None, 'petal_length': 7.5, 'petal_width': -999}
    answer = {'success': False, 'status': 'ParamsError', 'error': 'InvalidFeatureError'}

    response = request(method='GET', url=url, params=params)
    return_body = json.loads(response.text)

    assert response.status_code == 400
    assert return_body['success'] == answer['success']
    assert return_body['status'] == answer['status']
    assert return_body['error'] == answer['error']


if __name__ == '__main__':
    pass
