from sqlalchemy import select
from models import Autor, Livro
def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    if session.scalar(select(Autor).limit(1)) is not None:
        return
    escritor1 = Autor(nome="J.K. Rowling ", pais="Reino Unido")
    escritor2= Autor(nome=" Jenny Han", pais="Estado Unidos")
    escritor3 = Autor(nome="Kiera Cass", pais="Estado Unidos")
    session.add(escritor1)
    session.add_all([escritor2,escritor3])
    livros = [
        Livro(
            titulo="Harry Potter e a Pedra Filosofal",
            ano=1997,
            autor=escritor1,
            disponivel=True
        ),
        Livro(
            titulo="Harry Potter e a Câmara Secreta",
            ano=1881,
            autor=escritor1,
            disponivel=False
        ),
        Livro(
            titulo="Harry Potter e o Prisioneiro de Azkaban",
            ano=1998,
            autor=escritor1,
            disponivel=True
        ),
        Livro(
            titulo="Para Todos os Garotos que Já Amei",
            ano=2014,
            autor=escritor2,
            disponivel=True
        ),
        Livro(
            titulo="P.S. Ainda Amo Você",
            ano=2015,
            autor=escritor2,
            disponivel=False
        ),
        Livro(
            titulo="A Seleção",
            ano=2012,
            autor=escritor3,
            disponivel=True
        ),
    ]
    session.add_all(livros)
    session.commit()