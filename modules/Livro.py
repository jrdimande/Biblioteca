class Livro:
    def __init__(self, titulo, autor, copias_disponiveis = 0):
        self.titulo = titulo
        self.autor = autor
        self.copias_diponiveis = copias_disponiveis
        self.reservas = []

    def reservar(self, usuario):
        if self.copias_diponiveis > 0:
            self.reservas.append(usuario)
            self.copias_diponiveis -= 1
            print(f"Reserva confirmada para {usuario} do  livro {self.titulo}.")
        else:
            print(f"Desculpe, todas copias do livro {self.titulo} foram reservadas")

    def cancelar_reserva(self, usuario):
        if usuario in self.reservas:
            self.reservas.remove(usuario)
            self.copias_diponiveis += 1
        else:
            print(f"{usuario} não tem reserva no livro {self.reservas}")

    def verificar_disponibilidade(self):
        return self.copias_diponiveis



