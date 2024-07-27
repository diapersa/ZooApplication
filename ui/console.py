from domain.animal import Animal
from service.animal_service import AnimalService
from service.caretaker_service import CaretakerService
from service.statistics_service import StatisticsService


class ConsoleUI:
    def __init__(self, animal_service: AnimalService, caretaker_service: CaretakerService,
                 statistics_service: StatisticsService):
        self.__animal_service = animal_service
        self.__caretaker_service = caretaker_service
        self.__statistics_service = statistics_service

    def __print_menu(self):
        print("\nAplicatie Zoo\n\n"
              "Options:\n"
              "1.Add animal\n"
              "2.Delete animal\n"
              "3.Average zoo age\n"
              "4.Show all animals\n"
              "5.Add caretaker\n"
              "6.Delete caretaker\n"
              "7.Show all caretakers\n"
              "8.Show animals without caretaker\n"
              "0.Exit\n")

    def __validate_age(self, age: str):
        try:
            int(age)
        except Exception:
            raise ValueError("Age is not a number!")

    def __add_animal(self):
        name = input("Animal name: ")
        age = input("Animal age: ")

        self.__validate_age(age)

        self.__animal_service.add_animal(name, int(age))

    def __delete_animal(self):
        name = input("Animal name to delete : ")

        self.__animal_service.delete_animal(name)

    def __average_animal_age(self):
        print(f'The average age of all the animals is {self.__animal_service.get_average_animal_age()}')

    def __show_all_animals(self):
        for animal in self.__animal_service.get_all_animals():
            print(animal)

    def __add_caretaker(self):
        name = input("Caretaker name: ")
        age = input("Caretaker age: ")
        animal_name = input("Animal cared for: ")

        self.__validate_age(age)

        if not self.__animal_service.animal_exists(animal_name):
            raise Exception(f"There is no animal named {animal_name}")

        self.__caretaker_service.add_caretaker(name, int(age), animal_name)

    def __delete_caretaker(self):
        name = input("Caretaker name to delete : ")

        self.__caretaker_service.delete_caretaker(name)

    def __show_all_caretakers(self):
        for caretaker in self.__caretaker_service.get_all_caretakers():
            print(caretaker)

    def __show_animals_without_caretaker(self):
        for animal in self.__statistics_service.get_animals_without_caretaker():
            print(animal)

    def run(self):
        while True:
            self.__print_menu()
            try:
                command = int(input("Choose the command: ").strip())
                if command == 0:
                    break
                elif command == 1:
                    self.__add_animal()
                elif command == 2:
                    self.__delete_animal()
                elif command == 3:
                    self.__average_animal_age()
                elif command == 4:
                    self.__show_all_animals()
                elif command == 5:
                    self.__add_caretaker()
                elif command == 6:
                    self.__delete_caretaker()
                elif command == 7:
                    self.__show_all_caretakers()
                elif command == 8:
                    self.__show_animals_without_caretaker()
            except Exception as error:
                print(error)
