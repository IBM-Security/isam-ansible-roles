#!/usr/bin/python

"""
filter plugin with following features:
  1. filter takes a list 'a' and removes every tuple if the first value in the tuple matches a string 'b'
  2. filter takes a dict 'a' and recursivly calls himself to remove every tuple in a list matching 'b'

  e.g.
    - b='test'  |  [['test','value'], ['another','value']] ==> [['test','value']]
    - b=''      |  [['test','value'], ['another','value']] ==> [['test','value'], ['another','value']]
    - b='value' |  [['test','value'], ['another','value']] ==> []
    - b='another' |  [['test','value'], ['another','value']] ==> [['another','value']]
"""

from ansible import errors


def include_only(a, b):
    if isinstance(a,dict):
        for elem in a:
            if isinstance(a[elem],list):
                include_only(a[elem],b)
    if isinstance(a,list):
        for elem in list(a):
            if b != elem[0] and b != '':
                try:
                    a.remove(elem)
                except ValueError:
                    pass
    return a
class FilterModule(object):
    def filters(self):
        return {
            'include_only': include_only
        }
