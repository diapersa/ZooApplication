class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return "Name: {0}, Age: {1}".format(self.__name, self.__age)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_name() == other.get_name()