import whois    # подключаем модуль импорта 
w = whois.whois('tlock.ru') # смотрим в хуиз домена
p = whois.whois('puntolock.ru')
print (w['expiration_date'], w['domain_name']) # выводим дату и домен на экран
print (p['expiration_date'], p['domain_name'])
file_1 = open("export20.txt", "w")  # создаем файл для экспорта
file_1.write(str(w['domain_name'])) # операции записи, вместе с пробелами и переходом на вторую строку
file_1.write(' ')
file_1.write(str(w['expiration_date']))
file_1.write('\n')
file_1.write(str(p['domain_name']))
file_1.write(' ')
file_1.write(str(p['expiration_date']))
file_1.close()   #закрываем и сохраняем документ





#просто смотрим время выполнения
from datetime import datetime
import time
start_time = datetime.now()
time.sleep(1)
print(datetime.now() - start_time)


