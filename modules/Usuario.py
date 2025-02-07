class User:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.livros_reservados = []
        self.limite = 0
    def reservar_livro(self, livro):

        if len(self.livros_reservados) <= 3:
            self.livros_reservados.append(livro)
            print(f"{self.nome.title()} reservou o  livro {livro}")
            self.limite += 1
        else:
            print("Excedeu o limite de reservas")
    def cancelar_reserva(self, livro):
        if livro in self.livros_reservados:
            self.livros_reservados.remove(livro)
        else:
            print(f"Livro {livro} não encontrado na lista de reservas")

    def listar_reservas(self):
        return self.livros_reservados

    def informacao(self):
       for livro in self.livros_reservados:
           print(livro.autor)


