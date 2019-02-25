from functools import wraps

def curry(*types):
    def outerwrap(f):
        def innerwrap(*args):
            if len(types)>len(args):
                return curry(*(types[len(args):]))(lambda *largs: f(*args, *largs))
            return f(*args)
        return innerwrap
    return outerwrap
