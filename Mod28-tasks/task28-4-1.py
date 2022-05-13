class File:
    def __init__(self, file_name, file_mode):
        self.name = file_name
        self.mode = file_mode

    def __enter__(self):
           self.file = open(self.name, self.mode, encoding='utf-8')
           return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is FileExistsError:
            print('Указанный файл не существует')
        if exc_type is FileNotFoundError:
            print('Указанный файл не найден')
        return True


with File("example.txt", "w") as file:
    file.write('Всем привет!')