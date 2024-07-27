class Caretaker:
    def __init__(self, name, age, animal_name):
        self.__name = name
        self.__age = age
        self.__animal_name = animal_name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def get_animal_name(self):
        return self.__animal_name

    def set_animal_name(self, new_animal_name):
        self.__animal_name = new_animal_name

    def __str__(self):
        return "Name: {0}, Age: {1}, Animal name: {2}".format(self.__name, self.__age, self.__animal_name)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_name() == other.get_name()
