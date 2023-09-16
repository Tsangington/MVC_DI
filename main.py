from model import Model
from view import View
from controller import Controller
from config import Config

config = Config()
model = Model(config)
view = View()
controller = Controller( model, view, config)

