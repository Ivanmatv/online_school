class User:
    def __init__(self, name: str, type: str):
        self.__name = name
        self.__type = type

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type
