import logging

class View:
    def __init__(self) -> None:
        pass
    
    def ask_options(self):
        logging.info("Asking Options")
        print("-----------------------")
        print("1: show name")
        print("2: change name")
        print("3: exit")
        return(input("Choose your action: "))

    def ask_name(self):
        logging.info("Asking Name")
        print("-----------------------")
        return( input("What is your name? "))

    def show_name(self, data):
        logging.info("Showing Name")
        print("-----------------------")
        print(f"Your Name is: {data}!")

    def exit(self):
        logging.info("Exit")
        print("-----------------------")
        print("Exiting... Goodbye.")

    def invalid(self):
        logging.info("Invalid Choice")
        print("-----------------------")
        print("Invalid option, try again")