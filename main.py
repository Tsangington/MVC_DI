from model import Model
from view import View
from controller import Controller
from config import Config
import logging

logging.basicConfig(filename='logs.txt', encoding='utf-8', level=logging.DEBUG)

#Own Dependency injection?

if __name__ == "__main__":
    config = Config()
    model = Model(config)
    view = View()
    controller = Controller( model, view, config)
