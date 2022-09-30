import cx_Oracle

def getHost():
    arquivo = open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r')

    with open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r') as file:

        for line in file:

            aux = line[1:5]
            aux1 = line

            if aux == 'host':
                a = len(aux1)

                h = aux1[7:a]

                h = ''.join(h.split())

                host = h

                return host

    arquivo.close()


def getUser():
    arquivo = open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r')

    with open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r') as file:

        for line in file:

            aux = line[1:5]
            aux1 = line

            if aux == 'user':
                a = len(aux1)

                u = aux1[7:a]

                u = ''.join(u.split())

                user = u

                return user



    arquivo.close()


def getPassword():
    arquivo = open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r')

    with open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r') as file:

        for line in file:

            aux = line[1:9]
            aux1 = line

            if aux == 'password':
                a = len(aux1)

                p = aux1[11:a]

                p = ''.join(p.split())

                password = p

                return password

    arquivo.close()




def getDatabase():
     arquivo = open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r')

     with open('C:/Users/sj/PycharmProjects/parametros/Parameters.txt', 'r') as file:

          for line in file:

            aux = line[1:9]
            aux1 = line

            if aux == 'database':
                a = len(aux1)

                d = aux1[11:a]

                d = ''.join(d.split())

                database = d

                return database

     arquivo.close()