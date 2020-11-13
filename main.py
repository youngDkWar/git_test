active = True
error = "Ошибка: неверные данные. Помощь - help"
print('\n' + 'Добро пожаловать в интерактивный справочник, чтобы продолжить, введите "1"')
if input() != str(1):
    print(error[0:23:])
    active = False


def check(value):
    return  False


def Commands():
    print('\n' + 'Введите одну из следующих комманд:\n')
    print('create <название>  (создать новый справочник с названием)')
    print('add <имя_справочника> <имя> <фамилия> <телефон> <город> <email> (добавить запись в существующий справочник)')
    print('update <имя_справочника> <имя> <фамилия> <телефон> <город> <email>  (изменить существующую запись)')
    print('find <имя_справочника> <значение>  (найти существующую запись по любому значению(имя, фамилия и т.д.))')
    print('delete <имя_справочника> <имя> <фамилия> <телефон> <город> <email>  (удалить существующую запись)')
    print('exit  (закрыть интерактивный справочник)')
    print('\nПримечание: телефон и email являются уникальными значениями',
          '\n1) Нельзя создать запись с уже существующим в справочнике телефоном или почтой',
          '\n2) Нельзя однвременно изменить (update) телефон и почту\n')


def Create(value):
    if len(value) == 2:
        file = open(f"{value[1]}.txt", 'w')
        file.close()
        print(f"Справочник {value[1]} успешно создан")
    else:
        print(error)


def Add(value):
    if len(value) != 7:
        print(error)
        return
    if value[6].find("@") == -1:
        print("Ошибка: неврно указан email")
        return
    if Find([value[0], value[1], value[4], value[6]], 1) != "":
        print("Ошибка: человек с таким номером или почтой уже есть в справочнике")
        return
    file = open(f"{value[1]}", 'a')
    file.write(
        f"|  {value[2].lower().capitalize()} {value[3].lower().capitalize()} {value[4]} {value[5].lower().capitalize()} {value[6]}\n")
    file.close()
    print(f"Успешно. Запись добавлена в справочник '{value[1]}'")


def Find(value, p=0):
    if len(value) != 3 and p == 0:
        return "error"
    file = open(f"{value[1]}", 'r')
    temp = file.read().split('|')
    result = ""
    for s in temp:
        for e in s.split():
            if e.lower() == value[2]:
                result += s
    if result == "" and p != 0:
        for s in temp:
            for e in s.split():
                if e == value[3]:
                    result += s
    file.close()
    return result


def Update(value, p=""):
    file = open(f"{value[1]}", 'r')
    data = file.read().split('|')
    if Find([value[0], value[1], value[4], value[6]], 1) == "":
        print(error)
        return
    record_0 = Find([value[0], value[1], value[4], value[6]], 1).split()[-3]
    value = [value[0], value[1], value[2].capitalize(), value[3].capitalize(), value[4], value[5].capitalize(), value[6]]
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
    file = open(f"{value[1]}", 'w')
    file.write("|".join(data))
    file.close()
    print("Успешно\n")


while active:
    print('\nВведите комманду:  (help - помощь)')
    value, flag = input(), False
    for e in ["create", "add", "update", "find", "delete", "exit"]:
        if value:
            if e == value.split()[0] or value == "help":
                flag = True
                break
    if flag:
        if value == "help":
            Commands()
            continue
        value = value.split()
        if value[0] == 'exit':
            active = False
            continue
        if value[0] == 'create':
            Create(value)
            continue
        if value[0] == "add":
            Add(value)
            continue
        if value[0] == "update":
            Update(value)
            continue
        if value[0] == "find":
            result = Find(value)
            if result == "error":
                print(error)
            elif result != "":
                print(result)
            else:
                print("Не найден")
            continue
        if value[0] == "delete":
            Update(value, "1")
    else:
        print(error)
