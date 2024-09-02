import os

os.system("cls||clear")

class Livro:
    def __init__(self,titulo:str,autor:str,numerodepaginas:int,preco:float) -> None:

        self.titulo=titulo
        self.autor=autor
        self.numerodepaginas=numerodepaginas
        self.preco=preco

    def exibir_dados(self)->str:
        return f"\nNome:{self.titulo} \nAutor:{self.autor} \nNumero de Páginas: {self.numerodepaginas} \nPreço: {self.preco}"
        
primeiro_livro=Livro("IT a Coisa","Stephen King",1000,500)
segundo_livro=Livro("As Crônicas de Narnia","C.S Lewis",800,500)

print(primeiro_livro.exibir_dados())
print(segundo_livro.exibir_dados())

        

        