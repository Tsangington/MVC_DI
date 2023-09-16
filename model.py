from config import Config
import logging
class Model:
    def __init__(self, config: Config) -> None:
        self.database =  config.databasePath

    def save_text(self, text):
        logging.debug(f"Saving {text} to database")
        f = open( self.database, "w")
        f.write(f"{text}")
        f.close()
    
    def get_name(self):
        logging.debug(f"Reading text from database")
        f = open( self.database, "r")
        return (f.read())