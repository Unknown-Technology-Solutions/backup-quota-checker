class ec():
    ed = {
        "SEC600": "Internal server error",
        "CEC601": "Invalid enpoint requested",
        "CEC602": "Authentication failure",
        "CEC603": "Requested information doesn't exist"
    }
    def __setattr__(self, *_):
        raise SyntaxError