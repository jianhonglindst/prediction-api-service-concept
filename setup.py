# pylint: disable=C0301, R0913, R0903
# -*- encoding: utf-8 -*-
"""
@File    :  setup.py
@Time    :  2021/05/21 23:06:04
@Author  :  Lewis Lin
@Desc    :  
            $ pipenv run python setup.py develop --user
"""

from setuptools import setup
from setuptools import find_packages


setup(
    name='prediction_api_service',
    version='v1.0.0',
    description='prediction-api-service-concept',
    keywords='prediction, API, cherrypy',
    url='https://github.com/jianhonglindst/prediction-api-service-concept',
    packages=find_packages(),
    author='Lewis Lin',
    author_email='lewis.lin1134@gmail.com',
    tests_require=['pytest'],
)
