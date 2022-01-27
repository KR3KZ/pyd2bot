class SingletonError(Exception):
    def __init__(self, message, id):
        super().__init__(message)
        self.id = id