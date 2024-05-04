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

# Создание цикла и вложенного цикла согласно ТЗ пользователя XSS.is и вывод данных
for login_x in login:
    for password_x in password:
        print("Login: " + login_x, "Password: " + password_x)
# Создание цикла и вложенного цикла согласно ТЗ пользователя XSS.is и вывод данных
