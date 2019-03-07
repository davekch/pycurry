def curry(*types, exception=TypeError):
    def outerwrap(f):
        def innerwrap(*args):
            # check if types are correct
            for i in range(min(len(args),len(types))):
                if types[i] is Any:
                    continue
                if not type(args[i]) is types[i]:
                    raise exception("in {}: expected {}, got {}"\
                        .format(f.__name__, types[i], type(args[i])))
            # if too few arguments are given, return new curried function
            if len(types)>len(args):
                return curry(*(types[len(args):]))(lambda *largs: f(*args, *largs))
            return f(*args)
        return innerwrap
    return outerwrap

class Any:
    pass
