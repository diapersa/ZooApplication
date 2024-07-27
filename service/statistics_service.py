from repository.repository import Repository


class StatisticsService:
    def __init__(self, animal_repository: Repository, caretaker_repository: Repository):
        """
        Constructor for StatisticsService class
        :param animal_repository: animal repository (Repository)
        :param caretaker_repository: caretaker repository (Repository)
        :return:
        """
        self.__animal_repository = animal_repository
        self.__caretaker_repository = caretaker_repository

    def __has_caretaker(self, animal):
        """
        Checks if a given animal has a caretaker
        :param animal: animal to check (Animal)
        :return: True if the animal has a caretaker, False otherwise
        """
        caretaker_list = self.__caretaker_repository.get_all()
        for caretaker in caretaker_list:
            if caretaker.get_animal_name() == animal.get_name():
                return True
        return False

    def get_animals_without_caretaker(self):
        """
        Gets the list of all the animals without a caretaker
        :return: the list of all the animals without a caretaker (list)
        """
        animal_list = self.__animal_repository.get_all()
        no_caretaker_list = []
        for animal in animal_list:
            if not self.__has_caretaker(animal):
                no_caretaker_list.append(animal)
        return no_caretaker_list
