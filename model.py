
class Model:
    def __init__(self) -> None:
        pass

    def save_text(self, text):
        f = open("database.txt", "w")
        f.write(f"{text}")
        f.close()
    
    def get_name(self):
        f = open("database.txt", "r")
        return (f.read())