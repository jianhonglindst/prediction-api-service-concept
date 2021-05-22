# -*- encoding: utf-8 -*-
"""
# @File   : tools.py
# @TIME   : 2021-03-27 00:18:29
# @Author : Lewis Lin
# @Desc   : None

"""

__all__ = [
    'FileReader',
    'FileWriter'
]

import json


class FileReader:
    """ FileReader """

    @classmethod
    def html(cls, path: str):
        """ read html """
        with open(path, 'r') as _html:
            content = _html.read()
        return content

    @classmethod
    def json(cls, path: str):
        """ read json """
        with open(path, 'r') as _json:
            content = json.load(_json)
        return content


class FileWriter:
    """ FileWriter """

    @classmethod
    def json(cls, path: str, data: dict):
        """ write json """
        with open(path, 'w') as outfile:
            outfile.write(json.dumps(data, indent=4, sort_keys=True))
