'''
Created on 2017. dec. 8.

@author: User
'''
import os


class Root(object):

    @staticmethod
    def path():
        return os.path.dirname(__file__)

    @staticmethod
    def resources():
        return os.path.dirname(__file__) + "/resources/"

if __name__ == "__main__":
    print Root.path()
    print Root.resources()