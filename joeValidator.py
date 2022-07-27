from collections import namedtuple

User = namedtuple('User', ['login', 'senha'])

userAdm = User('espezzialy', 'abc')

def nameValidator(nome, password):
    if nome == userAdm.login:
        if senha == userAdm.senha:
            print("Acesso garantido")
            return True
        else:
            print("Senha incorreta")
    else:
        print("User invalido")
    return False



while True:
    print("digite seu nome")
    name = input()
    print("Digite sua senha")
    senha = input()
    if nameValidator(name, senha):
        break
    else:
        print("Tente novamente")
