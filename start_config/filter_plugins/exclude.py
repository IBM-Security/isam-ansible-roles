#!/usr/bin/python

from ansible import errors

def exclude(a, b):
    temp = a.copy()
    if isinstance(a,dict):
        temp.pop(b, None)
    return temp
class FilterModule(object):
    def filters(self):
        return {
            'exclude': exclude
        }