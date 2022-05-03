class File:
    def __init__(self, file_name: str, mode: str) -> None:
        self.__file_name = file_name
        self.__mode = mode

    def __enter__(self):
        try:
            self.__file = open(self.__file_name, self.__mode, encoding='utf-8')
        except FileNotFoundError:
            self.__file = open(self.__file_name, 'w')
            self.__file = open(self.__file_name, self.__mode, encoding='utf-8')
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is FileNotFoundError or exc_type is FileExistsError:
            return True
        self.__file.close()


with File('example.txt', 'r') as file:
    text = file.read().split()
with File('example.txt', 'w') as file:
    file.write('Всем привет!')