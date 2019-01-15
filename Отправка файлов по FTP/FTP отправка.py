from pathlib import Path
from ftplib import FTP

spis = []
pyt='U:\content'
path_to_file = Path(pyt)
for name_file in path_to_file.glob('*.*'):
    spis.append(name_file.name)
print(list(spis))

host = "127.0.0.1"
port = 2121
user = "anonymous"
password = "123"
#con = FTP(host,user,password)
#print('Подключился к серверу')
#con.close
#print('Подключение разорано')

k=''
ftp = FTP()
print('Подключение')
ftp.connect(host,port)
print('Логин Пароль')
ftp.login(user,password)
print('Подключился к серверу')
for name_file1 in spis:
    k = pyt+'/'+name_file1
    f = open(k,"rb")
    send = ftp.storbinary("STOR "+ name_file1, f)
    k='';
ftp.close
print('Подключение разорано')
