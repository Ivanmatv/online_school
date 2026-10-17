class User:
    def __init__(self, name: str, user_type: str):
        self.__name = name
        self.__user_type = user_type

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__user_type
