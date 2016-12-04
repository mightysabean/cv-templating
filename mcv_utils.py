import os

# MIT Licence
def getVariableFromList(search_dict, l):
    dc = search_dict.copy()
    for k in l:
        dc = dc.get(k)
    return dc

def fullname(name, family):
    return name + ' ' + family

# Extracted from stackoverflow
def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy.
    http://stackoverflow.com/a/26853961"""
    z = x.copy()
    z.update(y)
    return z

# Extracted from stackoverflow
def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    http://stackoverflow.com/a/26853961
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

