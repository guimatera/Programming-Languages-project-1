
class Aluno():
    def __init__(self, user, senha):
        self.__user = user
        self.__senha = senha
    def set_password(self, senha):
        self.__senha = senha
    def set_name(self, nome):
        self.__nome = nome
    def get_password(self):
        return self.__senha
    def get_user(self):
        return self.__user
    def save(self):
        registro = self.__user + ' - ' + self.__senha +'\n'
        arquivo = open('cadastro.txt','a')
        arquivo.writelines(registro)




    

