from config import Config
class Model:
    def __init__(self, config: Config) -> None:
        self.database =  config.databasePath

    def save_text(self, text):
        f = open( self.database, "w")
        f.write(f"{text}")
        f.close()
    
    def get_name(self):
        f = open( self.database, "r")
        return (f.read())