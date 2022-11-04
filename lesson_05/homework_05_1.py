from colors import bcolors


class File:
    def __init__(self, filename, mode, color):
        self.filename = filename
        self.mode = mode
        self.color = color
        self.default_color = bcolors.ENDC

    def __enter__(self):
        print(f"Opening the file {self.filename}.{self.color}")
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"{self.default_color}Closing the file {self.filename}.")
        if not self.__file.closed:
            self.__file.close()
        return False


with File("some_file.txt", "r", bcolors.OKBLUE) as file:
    print(file.read())
