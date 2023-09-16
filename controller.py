from view import View
from model import Model
from config import Config

class Controller:
    def __init__(self, model: Model, view: View, config: Config) -> None:
        self.model = model
        self.view = view
        self.config = config

        model.save_text(view.ask_name())
        while True:
            option = view.ask_options()
            if option == "1":
                view.show_name(model.get_name())
            elif option == "2":
                model.save_text(view.ask_name())
            elif option == "3":
                view.exit()
                break
            else:
                view.invalid()
