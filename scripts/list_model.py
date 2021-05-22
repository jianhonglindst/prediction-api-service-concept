# pylint: disable=C0301, R0913, R0903
# -*- encoding: utf-8 -*-
"""
@File    :  list_model.py
@Time    :  2021/05/21 22:51:10
@Author  :  Lewis Lin
@Desc    :  generate model list
"""

import pathlib

from src.tools import FileWriter

def main():
    """ list models to a json file """
    model_paths = list(pathlib.Path('models').glob('*.pkl'))
    model_dt = {}
    for model in model_paths:
        key_name = model.name.split('.pkl')[0]
        key_name = key_name.replace('-', '_')
        model_dt[key_name] = str(model)

    FileWriter.json(path='model.json', data=model_dt)


if __name__ == '__main__':
    main()
