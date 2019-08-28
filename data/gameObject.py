class GameObject:
    def __init__(self, object_type, id, name, definition):
        self.__object_type = object_type
        self.__definition = definition
        self.__identifier = id
        self.__name = name

    @property
    def identifier(self):
        return self.__identifier

    @property
    def name(self):
        return self.__name

    @property
    def object_type(self):
        return self.__object_type

    @property
    def definition(self):
        return self.__definition
