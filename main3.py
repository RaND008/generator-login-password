

# Открываем TXT с логинами и создаем список
filename_login = "login.txt"
with open(filename_login, 'r') as f:
    login = [line.rstrip('\n') for line in f] # Генерация списка пользователей с удалением перехода символа строки \n
# Открываем TXT с логинами и создаем список

# Открываем TXT с паролями и создаем список
filename_password = "password.txt"
with open(filename_password, 'r') as f:
    password = [line.rstrip('\n') for line in f] # Генерация списка паролей с удалением перехода символа строки \n
# Открываем TXT с паролями и создаем список


#Добавление "" на login и password
l = [] # Создание пустого списка для работы с ним в цикле (Login)
p = [] # Создание пустого списка для работы с ним в цикле (Password)
# Создание цикла и вложенного цикла согласно ТЗ пользователя XSS.is и вывод данных
for login_x in login:
    for password_x in password:
        login_spisok_tz = l.append(login_x)
        for password_y in login:
            password_spisok_tz = p.append(password_x)
            break
# Создание цикла и вложенного цикла согласно ТЗ пользователя XSS.is и вывод данных

# Преобразование списков в строку
Spisok_loginov = l
Spisok_password = p
razdelitel_stroki = ","
login_stroka = razdelitel_stroki.join(Spisok_loginov)
password_stroka = razdelitel_stroki.join(Spisok_password)
#print(login_stroka)
#print(password_stroka)
#Добавление "" на login и password
p = []
l = []
#Добавление ""
for x in Spisok_loginov:
    login_format = ''.join(('"', x, '"'))
    login_list = l.append(login_format)

for y in password:
    login_password = ''.join(('"', y, '"'))
    password_list = p.append(login_password)
# Добавление ""
# Преобразование списков в строку
Spisok_loginov = l
Spisok_password = p
razdelitel_stroki = ", "

login_stroka = razdelitel_stroki.join(Spisok_loginov)
password_stroka = razdelitel_stroki.join(Spisok_password)
count = 0
password_obrezka = len(password_stroka) // len(password)

for i in range(len(login)):
    with open("output.txt", "a") as f:
        login_out = ('"' + login[count] + '"' + ',' + " ") * len(password)
        print(login_out[:-2], file=f)
        count += 1
    with open("output.txt", "a") as f:
        print(password_stroka + "\n", file=f)
