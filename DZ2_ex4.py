# Сформировать из  этих имен и вывести на экран фразы типа "Привет Игорь!"

personal = ['инженер-конструктор игорь', 'главный бухгалтер МАРИНА', 'токарь вышего разряда нИКОЛАй', 'Директор аэлита']
for i in range(len(personal)):
    name = personal[i]
    print(f'Привет! {name.split()[-1].title()}')