

def get_variables(arg):
    """
    @param arg: is a dictionary of configurations, or a module with the configurations
    """
    params = dict()
    if isinstance(arg, dict):
        variables = arg
    else:
        variables = dict((var, getattr(arg, var)) for var in dir(arg))

    for variable, value in variables.items():
        # don't include system variables, methods, classes, modules
        if not variable.startswith("__") and \
                not hasattr(value, '__call__') and \
                not hasattr(value, '__file__'):
            params[variable] = value
    return params



import mymodule
print(get_variables(mymodule))