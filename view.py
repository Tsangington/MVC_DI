class View:
    def __init__(self) -> None:
        pass
    
    def ask_options(self):
        print("-----------------------")
        print("1: show name")
        print("2: change name")
        print("3: exit")
        return(input("Choose your action: "))

    def ask_name(self):
        print("-----------------------")
        return( input("What is your name? "))

    def show_name(self, data):
        print("-----------------------")
        print(f"Your Name is: {data}!")

    def exit(self):
        print("-----------------------")
        print("Exiting... Goodbye.")

    def invalid(self):
        print("-----------------------")
        print("Invalid option, try again")