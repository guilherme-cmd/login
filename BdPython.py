import pymysql
import dados
import login

log = login.Name()
sen = login.Senha()
conexao = pymysql.connect(
      host=dados.getHost(),
      user=dados.getUser(),
      password=dados.getPassword(),
      database=dados.getDatabase()
)
cursor = conexao.cursor()
x = cursor.execute("select * from GDS_FUNCIONARIOS WHERE USUARIO = %log AND SENHA = %sen ")

resultado = cursor.fetchall()

for x in resultado:
   print(x)
