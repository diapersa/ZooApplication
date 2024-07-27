from domain.animal import Animal
from repository.repository import Repository


class AnimalService:
    def __init__(self, repository: Repository):
        """
        Constructor for AnimalService class
        :param repository: animal repository (Repository)
        :return:
        """
        self.__repository = repository

    def add_animal(self, name, age):
        """
        Adds an animal to the animal list if it does not exist
        :param name: name of the animal (str)
        :param age: age of the animal (int)
        :return:
        """
        animal = Animal(name, age)
        self.__repository.add(animal)

    def animal_exists(self, animal_name):
        """
        Checks if an animal with a given name exists
        :param animal_name: name of the animal (str)
        :return: True if animal exists, False otherwise
        """
        return self.__repository.find_position(Animal(animal_name, 0)) is not None

    def delete_animal(self, name):
        """
        Deletes an animal with a given name
        :param name: name of the animal (str)
        :return:
        """
        animal = Animal(name, 0)
        self.__repository.delete(animal)

    def get_all_animals(self):
        """
        Returns the list containing all the animals
        :return: The list of all the animals (list)
        """
        return self.__repository.get_all()

    def get_average_animal_age(self):
        """
        Returns the average of all the animals in the list
        :return: The average age of all the animals (float)
        """
        animal_list = self.__repository.get_all()
        age_sum = 0
        for animal in animal_list:
            age_sum += animal.get_age()
        return age_sum / len(animal_list)
