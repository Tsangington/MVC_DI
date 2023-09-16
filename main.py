from model import Model
from view import View
from controller import Controller
from config import Config
import logging
from dependency_injector import containers
from .containers import Container

logging.basicConfig(filename='logs.txt', encoding='utf-8', level=logging.DEBUG)

#Own Dependency injection?
def main():
    config = Config()
    model = Model(config)
    view = View()
    controller = Controller( model, view, config)

if __name__ == "__main__":
    #container = Container()

    main()