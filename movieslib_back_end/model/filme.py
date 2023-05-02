from sqlalchemy import Column, String, Integer, DateTime  # Float removido
from datetime import datetime
from typing import Union

from  model import Base

class Filme(Base):
    __tablename__ = 'filme'

    id = Column("pk_filme", Integer, primary_key=True)
    titulo = Column(String(40), unique=True)
    tipo = Column(String(20))
    media = Column(String(15))
    info = Column(String(2000))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, titulo:str, tipo:str, media:str, info:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma entrada para Filme
        Argumentos:
            titulo: título do filme.
            tipo: tipo de filme. Exemplo: Aventura, Comédia, Drama, Ficção, Ficção Científica, Suspense, Terror, Western, etc
            media: mídia na qual o filme se encontra. Exemplo: DVD, HDD, Blu-Ray Disc, AppleTV, AmazonPrime, Now, etc
            info: informações sobre o filme, tais como atores, diretor, aspectos genéricos do filme, etc
            data_insercao: data de inserção do filme à base de dados
        """
        self.titulo = titulo
        self.tipo = tipo
        self.media = media
        self.info = info

        # Se a data de inserção for informda, então ela é inserida. 
        # Se não, será usada a data exata da inserção dos demais dados no banco de dados
        if data_insercao:
            self.data_insercao = data_insercao
