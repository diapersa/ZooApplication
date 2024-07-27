from domain.animal import Animal
from domain.caretaker import Caretaker
from repository.repository import Repository
from service.animal_service import AnimalService
from service.caretaker_service import CaretakerService
from service.statistics_service import StatisticsService
from ui.console import ConsoleUI

animal_repository = Repository([Animal("Rex", 4), Animal("Miti", 6), Animal("Gusti", 8)])
caretaker_repository = Repository([Caretaker("Mihai", 40, "Rex"), Caretaker("Abel", 25, "Miti")])

animal_service = AnimalService(animal_repository)
caretaker_service = CaretakerService(caretaker_repository)
statistics_service = StatisticsService(animal_repository, caretaker_repository)

ui = ConsoleUI(animal_service, caretaker_service, statistics_service)

ui.run()
