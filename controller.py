from view import View
from model import Model
from config import Config
import logging

class Controller:
    def __init__(self, model: Model, view: View, config: Config) -> None:
        # Manual Dependency Injection:
        # self.model = Model()
        # self.view = view()
        # self.config = config()
        
        self.model = model #Dependency injection
        self.view = view #Dependency injection
        self.config = config #Dependency injection

        logging.info("Start")
        model.save_text(view.ask_name())
        while True:
            option = view.ask_options()
            logging.debug(f"Option choice:{option}")

            if option == "1":
                name = view.show_name(model.get_name())

            elif option == "2":
                name = model.save_text(view.ask_name())

            elif option == "3":
                view.exit()
                logging.info("Finished")
                break
            else:
                view.invalid()
