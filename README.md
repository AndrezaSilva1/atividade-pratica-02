# Atividade Prática 02 - Biblioteca Persistente
Complete os arquivos da base usando SQLAlchemy ORM.
## Como executar
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```
## Defesa escrita
Responda ao final:
1. Para que serve o campo `disponivel` em `Livro`? Server para indicar se o livro esta disponivel para emprestimo.
2. Por que é necessário chamar `session.commit()` após emprestar ou devolver? Para salvar alterações de banco de dados.
3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?No tipo de consulta listar_livros, usando livro.autor.nome.

