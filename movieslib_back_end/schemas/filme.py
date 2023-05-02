from pydantic import BaseModel
from typing import List # Optional retirdo
from model.filme import Filme

class FilmeSchema(BaseModel):
    # Como um novo filme deve ser representado
    titulo: str = "Menina de Ouro"
    tipo: str = "Drama"
    media: str = "DVD"
    info: str = ""


class FilmeBuscaSchema(BaseModel):
    # Estrutura que realiza a busca. Baseia-se no nome do filme.
    titulo: str = "Teste"


class ListagemFilmesSchema(BaseModel):
    # Como os filmes armazenados serão retornados
    filmes:List[FilmeSchema]


def apresenta_filmes(filmes: List[Filme]):
    # Apresenta o filme, conforme definido em FilmeViewSchema.
    result = []
    for filme in filmes:
        result.append({
            "titulo": filme.titulo,
            "tipo": filme.tipo,
            "media": filme.media,
            "info": filme.info,
        })

    return {"filmes": result}


class FilmeViewSchema(BaseModel):
    # Como um filme será retornado
    id: int = 1
    titulo: str = "Menina de Ouro"
    tipo: str = "Drama"
    media: str = "DVD"
    info: str = ""

class FilmeDelSchema(BaseModel):
    # Retorna o nome do filme removido, com uma mensagem
    message: str
    titulo: str

def apresenta_filme(filme: Filme):
    # Retorna um filme, conforme o definido em FilmeViewSchema
    
    return {
        "id": filme.id,
        "titulo": filme.titulo,
        "tipo": filme.tipo,
        "media": filme.media,
        "info": filme.info,
    }
