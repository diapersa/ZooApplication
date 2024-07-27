from domain.caretaker import Caretaker
from repository.repository import Repository


class CaretakerService:
    def __init__(self, repository: Repository):
        """
        Constructor for CaretakerService class
        :param repository: caretaker repository (Repository)
        :return:
        """
        self.__repository = repository

    def add_caretaker(self, name, age, caretaker_name):
        """
        Adds a caretaker to the caretaker list if it does not exist
        :param name: name of the caretaker (str)
        :param age: age of the caretaker (int)
        :param caretaker_name: age of the caretaker (str)
        :return:
        """
        caretaker = Caretaker(name, age, caretaker_name)
        self.__repository.add(caretaker)

    def delete_caretaker(self, name):
        """
        Deletes a caretaker with a given name
        :param name: name of the caretaker (str)
        :return:
        """
        caretaker = Caretaker(name, 0, "")
        self.__repository.delete(caretaker)

    def get_all_caretakers(self):
        """
        Returns the list containing all the caretakers
        :return: The list of all the caretakers (list)
        """
        return self.__repository.get_all()

