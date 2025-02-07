from modules.Usuario import *
from modules.Livro import *

# Criação de livros
livro1 = Livro("1984", "George Orwell", 5)
livro2 = Livro("Brave New World", "Aldous Huxley", 2)

# Criação de usuários
usuario1 = User("Alice", 101)
usuario2 = User("Bob", 102)

# Reservar livros
usuario1.reservar_livro(livro1)
usuario1.reservar_livro(livro2)
usuario2.reservar_livro(livro1)

# Verificar disponibilidade de cópias
print(livro1.verificar_disponibilidade())

# Cancelar reserva
usuario1.cancelar_reserva(livro1)

# Verificar disponibilidade de cópias após o cancelamento
print(livro1.verificar_disponibilidade())

# Listar reservas do usuário
print(usuario1.listar_reservas())

print(usuario2.listar_reservas())

