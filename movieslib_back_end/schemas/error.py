from pydantic import BaseModel

class ErrorSchema(BaseModel):
    # Retorna a mensagem de erro
    message: str
