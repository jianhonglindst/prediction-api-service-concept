# -*- encoding: utf-8 -*-
"""
# @File   : app.py
# @TIME   : 2021-03-27 00:09:09
# @Author : Lewis Lin
# @Desc   :
"""


import cherrypy

from src.tools import FileReader

# api
from src.api import PredictCategoryIRIS


__index_html__ = FileReader.html('index.html')
__model__ = FileReader.json('model.json')


class Root:
    """Root
    """
    @cherrypy.expose
    def index(self):
        """ index """
        return __index_html__


if __name__ == '__main__':
    cherrypy.config.update(config='cherrypy.conf')
    cherrypy.tree.mount(Root())

    cherrypy.tree.mount(
        root=PredictCategoryIRIS(model=__model__),
        script_name='/predict/category/iris',
        config={
            '/':
                {
                    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                    "tools.response_headers.on": True,
                    'tools.response_headers.headers': [('Access-Control-Allow-Origin', '*')]
                }
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
