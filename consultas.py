from sqlalchemy import select
from models import Autor, Livro
def listar_livros(session):
    """Liste todos os livros com autor e disponibilidade."""
    livros = session.scalars(select(Livro)).all()
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"{livro.titulo} | Autor: {livro.autor.nome} | {status}")
    return livros
def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    consulta = select(Livro).where(Livro.disponivel == True)
    livros = session.scalars(consulta).all()
    for livro in livros:
        print(f"{livro.titulo} | Autor: {livro.autor.nome}")
    return livros
def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    consulta = select(Livro).where(Livro.titulo.contains(trecho))
    livros = session.scalars(consulta).all()
    for livro in livros:
        print(livro.titulo)
    return livros
def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    consulta = select(Autor).where(Autor.nome == nome_autor)
    autor = session.scalar(consulta)
    if autor is None:
        print("Autor achado.")
        return []
    for livro in autor.livros:
        print(livro.titulo)
    return autor.livros
