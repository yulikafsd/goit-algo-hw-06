class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class SearchError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)