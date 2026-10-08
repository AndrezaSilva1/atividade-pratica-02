from sqlalchemy import select
from models import Livro
def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    consulta = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalar(consulta)
    if livro is None:
        print("Livro não achado")
        return

    if not livro.disponivel:
        print("O livro esta disponivel")
        return
    livro.disponivel = False
    session.commit()
    print("Livro foi emprestado com sucesso.")
def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    consulta = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalar(consulta)
    if livro is None:
        print("O livro não foi achado")
        return
    if livro.disponivel:
        print("O livro já esta disponivel")
        return
    livro.disponivel = True
    session.commit()
    print("o livro foi devolvido com secesso.")