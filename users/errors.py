class Error(Exception):
    # Base class
    pass

class NoValueError(Error):
    def __init__(self, var, message = 'this variable is empty and should not be!', *args):
        self.var = var
        self.message = message
        self.args = args

    def __str__(self):
        return '{} : {}'.format(self.var, self.message)
