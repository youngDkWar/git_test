class Dictionary:
    __active__ = True
    __error__ = "Ошибка: неверные данные. Помощь - help"

    def start(self):
        print('\n' + 'Добро пожаловать в интерактивный справочник, чтобы продолжить, введите "1"')
        if input() != str(1):
            print(self.__error__[0:23])
            self.__active__ = False
        self.__cycle__()

    def create(self, value):
        if len(value) == 2:
            file = open(f"{value[1]}.txt", 'w')
            file.close()
            print(f"Справочник {value[1]} успешно создан")
        else:
            print(self.__error__)

    @staticmethod
    def commands():
        print('\n' + 'Введите одну из следующих комманд:\n')
        print('create <название>  (создать новый справочник с названием)')
        print(
            'add <имя_справочника> <имя> <фамилия> <телефон> <город> <email> '
            '(добавить запись в существующий справочник)')
        print('update <имя_справочника> <имя> <фамилия> <телефон> <город> <email>  (изменить существующую запись)')
        print('find <имя_справочника> <значение>  (найти существующую запись по любому значению(имя, фамилия и т.д.))')
        print('delete <имя_справочника> <имя> <фамилия> <телефон> <город> <email>  (удалить существующую запись)')
        print('exit  (закрыть интерактивный справочник)')
        print('\nПримечание: телефон и email являются уникальными значениями',
              '\n1) Нельзя создать запись с уже существующим в справочнике телефоном или почтой',
              '\n2) Нельзя однвременно изменить (update) телефон и почту\n')

    @staticmethod
    def find(value, p=0):
        if len(value) != 3 and p == 0:
            return "error"
        file = open(f"{value[1]}.txt", 'r')
        temp = file.read().split('|')
        result = "".join([s for s in temp for e in s.split() if e.lower() == value[2]])
        if result == "" and p != 0:
            result = "".join([s for s in temp for e in s.split() if e == value[3]])
        file.close()
        return result

    def add(self, value):
        if len(value) != 7:
            print(self.__error__)
            return
        if value[6].find("@") == -1:
            print("Ошибка: неврно указан email")
            return
        if self.find([value[0], value[1], value[4], value[6]], 1) != "":
            print("Ошибка: человек с таким номером или почтой уже есть в справочнике")
            return
        file = open(f"{value[1]}.txt", 'a')
        file.write(
            f"|  {value[2].lower().capitalize()} {value[3].lower().capitalize()} "
            f"{value[4]} {value[5].lower().capitalize()} {value[6]}\n")
        file.close()
        print(f"Успешно. Запись добавлена в справочник '{value[1]}'")

    def update(self, value, p=""):
        file = open(f"{value[1]}.txt", 'r')
        data = file.read().split('|')
        if self.find([value[0], value[1], value[4], value[6]], 1) == "":
            print(self.__error__)
            return
        record_0 = self.find([value[0], value[1], value[4], value[6]], 1).split()[-3]
        value = [value[0], value[1], value[2].capitalize(), value[3].capitalize(), value[4], value[5].capitalize(),
                 value[6]]
        record_1 = "  " + " ".join(value[2::]) + "\n"
        index = ""
        for i in range(len(data)):
            for el in data[i].split():
                if el == record_0:
                    index = i
        if p != "":
            data[index] = ""
        else:
            data[index] = record_1
        file.close()
        file = open(f"{value[1]}.txt", 'w')
        file.write("|".join(data))
        file.close()
        print("Успешно\n")

    def __cycle__(self) -> None:
        while self.__active__:
            print('\nВведите комманду:  (help - помощь)')
            value, flag = input(), False
            for e in ["create", "add", "update", "find", "delete", "exit"]:
                if value:
                    if e == value.split()[0] or value == "help":
                        flag = True
                        break
            if flag:
                if value == "help":
                    self.commands()
                    continue
                value = value.split()
                if value[0] == 'exit':
                    self.__active__ = False
                    continue
                if value[0] == 'create':
                    self.create(value)
                    continue
                if value[0] == "add":
                    self.add(value)
                    continue
                if value[0] == "update":
                    self.update(value)
                    continue
                if value[0] == "find":
                    result = self.find(value)
                    if result == "error":
                        print(self.__error__)
                    elif result != "":
                        print(result)
                    else:
                        print("Не найден")
                    continue
                if value[0] == "delete":
                    self.update(value, "1")
            else:
                print(self.__error__)
