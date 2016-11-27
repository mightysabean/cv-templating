import os

def output_dir(base, dir):
    """Full path a directorio de salida. Si no existe se crea"""
    f= os.path.join(base, dir) \
        if dir != '' or dir is None \
        else base
    if not os.path.exists(f):
        os.mkdir(f)
    return f

def fullname(name, family):
    return name + ' ' + family

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy.
    http://stackoverflow.com/a/26853961"""
    z = x.copy()
    z.update(y)
    return z