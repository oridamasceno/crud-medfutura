from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class Pessoa(BaseModel):
    apelido: str = Field(..., max_length=32)
    nome: str = Field(..., max_length=100)
    nascimento: date
    stack: Optional[List[str]] = Field(default=[])

class PessoaResponse(Pessoa):
    id: int
