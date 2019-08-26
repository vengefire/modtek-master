class GameObject:
    def __init__(self, object_type, definition):
        self.__object_type = object_type
        self.__definition = definition

    @property
    def object_type(self):
        return self.__object_type

    @property
    def definition(self):
        return self.__definition
