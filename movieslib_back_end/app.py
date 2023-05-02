from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Filme
from logger import logger
from schemas import *
from flask_cors import CORS

infor = Info(title="API para MoviesLib", version="1.0.1")
app = OpenAPI(__name__, info=infor)
CORS(app)

# definição das tags
home_tag = Tag(name="Documentação", description="Seleção de tipo de documentação: Swagger, Redoc ou RapiDoc")
filme_tag = Tag(name="Filme", description="Inserção, visualização e remoção de filmes da base de dados")

@app.get('/', tags=[home_tag])
def home():
    #Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    return redirect('/openapi')


@app.post('/filme', tags=[filme_tag], responses={"200": FilmeViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_filme(form: FilmeSchema):
    """Adiciona um novo Filme à base de dados
       Retorna os filmes inseridos
    """
    filme = Filme(
        titulo=form.titulo,
        tipo=form.tipo,
        media=form.media,
        info=form.info)
    
    logger.debug(f"Adicionando filme de título: '{filme.titulo}'")
    try:
        # cria conexão com a base
        session = Session()
        # adiciona filme
        session.add(filme)
        # efetiva o comando de inserção de novo filme à tabela "filme" do banco de dados
        session.commit()
        logger.debug(f"Adicionado filme de título: '{filme.titulo}'")
        return apresenta_filme(filme), 200

    except IntegrityError as e:
        # Duplicidade de titulo
        error_msg = "Título já existente :/"
        logger.warning(f"Erro ao adicionar filme '{filme.titulo}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # Erro fora do previsto
        error_msg = "Não foi possível adicionar novo filme :/"
        logger.warning(f"Erro ao adicionar filme '{filme.titulo}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/filmes', tags=[filme_tag], responses={"200": ListagemFilmesSchema, "404": ErrorSchema})
def get_filmes():
    """Faz a busca por todos os Filmes cadastrados
    Retorna-os na listagem de filmes.
    """
    logger.debug(f"Coletando filmes ")
    # cria conexão com a base
    session = Session()
    # faz a busca
    filmes = session.query(Filme).all()

    # se não há filmes cadastrados
    if not filmes:
        return {"filmes": []}, 200
    else:
        logger.debug(f"%d filmes encontrados" % len(filmes))
        # retorna a representação de filmes
    #    print(filmes) #????
        return apresenta_filmes(filmes), 200


@app.get('/filme', tags=[filme_tag], responses={"200": FilmeViewSchema, "404": ErrorSchema})
def get_filme(query: FilmeBuscaSchema):
    """Faz a busca por um Filme a partir de seu id
    Retorna o filme
    """
    filme_id = query.id
    logger.debug(f"Coletando dados sobre filme #{filme_id}")
    # cria conexão com a base
    session = Session()
    # faz a busca
    filme = session.query(Filme).filter(Filme.id == filme_id).first()

    # se o filme não foi encontrado
    if not filme:
        error_msg = "Filme não encontrado na base de dados :/"
        logger.warning(f"Erro ao buscar filme '{filme_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Filme econtrado: '{filme.titulo}'")
        # retorna o filme
        return apresenta_filme(filme), 200


@app.delete('/filme', tags=[filme_tag], responses={"200": FilmeDelSchema, "404": ErrorSchema})
def del_filme(query: FilmeBuscaSchema):
    """Deleta um Filme a partir do id informado
    Retorna uma mensagem de confirmação da remoção
    """
    filme_titulo = unquote(unquote(query.titulo))
    logger.debug(f"Deletando dados sobre filme #{filme_titulo}")
    # cria conexão com a base
    session = Session()
    # faze a remoção
    count = session.query(Filme).filter(Filme.titulo == filme_titulo).delete()
    session.commit()

    if count:
        # retorna a mensagem de confirmação
        logger.debug(f"Deletado filme {filme_titulo}")
        return {"message": "Filme removido", "id": filme_titulo}
    else:
        # se o filme não foi encontrado
        error_msg = "Filme não encontrado na base de dados :/"
        logger.warning(f"Erro ao deletar filme '{filme_titulo}', {error_msg}")
        return {"message": error_msg}, 404

