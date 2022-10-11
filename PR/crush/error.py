class NotPathError(Exception):
    def __int__(self, message):
        self.message = message


class FromError(Exception):
    def __int__(self, message):
        self.message = message


class SizeError(Exception):
    def __int__(self, message):
        self.message = message
