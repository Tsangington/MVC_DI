from view import View
from model import Model

class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
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
                print("Invalid Option, try again")
