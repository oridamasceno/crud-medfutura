from fastapi import APIRouter, HTTPException, Query
from .models import Pessoa, PessoaResponse
from .database import get_db_connection
from typing import List
import pyodbc
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/pessoas", response_model=PessoaResponse, status_code=201)
async def create_pessoa(pessoa: Pessoa):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        logger.info("Iniciando a inserção dos dados.")
        
        # Inserir dados na tabela Pessoas
        cursor.execute("""
            INSERT INTO Pessoas (apelido, nome, nascimento, stack)
            OUTPUT inserted.id
            VALUES (?, ?, ?, ?)
        """, pessoa.apelido, pessoa.nome, pessoa.nascimento, ','.join(pessoa.stack))
        
        # Recuperar o ID gerado
        result = cursor.fetchone()
        id = result[0] if result else None
        logger.info(f"ID gerado: {id}")

        # Verificar se o ID foi gerado corretamente
        if id is None:
            raise HTTPException(status_code=500, detail="Erro ao gerar ID")

        conn.commit()
        
        # Retornar a resposta com o ID
        return PessoaResponse(id=id, **pessoa.dict())

    except pyodbc.IntegrityError as e:
        logger.error(f"Erro ao criar pessoa: {e}")
        raise HTTPException(status_code=422, detail="Apelido já existe ou dados inválidos")
    except Exception as e:
        logger.error(f"Erro ao criar pessoa: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
    finally:
        conn.close()

@router.get("/pessoas/{id}", response_model=PessoaResponse)
def get_pessoa(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    pessoa = cursor.execute("SELECT * FROM Pessoas WHERE id=?", id).fetchone()
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return {
        "id": pessoa.id,
        "apelido": pessoa.apelido,
        "nome": pessoa.nome,
        "nascimento": pessoa.nascimento,
        "stack": pessoa.stack.split(',')
    }

@router.get("/pessoas", response_model=List[PessoaResponse])
def search_pessoas(t: str = Query(..., description="Termo de busca")):
    conn = get_db_connection()
    cursor = conn.cursor()
    pessoas = cursor.execute("""
        SELECT * FROM Pessoas
        WHERE apelido LIKE ? OR nome LIKE ? OR stack LIKE ?
    """, f'%{t}%', f'%{t}%', f'%{t}%').fetchall()
    return [
        {
            "id": p.id,
            "apelido": p.apelido,
            "nome": p.nome,
            "nascimento": p.nascimento,
            "stack": p.stack.split(',')
        } for p in pessoas
    ]

@router.put("/pessoas/{id}", response_model=PessoaResponse)
def update_pessoa(id: int, pessoa: Pessoa):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Pessoas SET apelido=?, nome=?, nascimento=?, stack=?
        WHERE id=?
    """, pessoa.apelido, pessoa.nome, pessoa.nascimento, ','.join(pessoa.stack), id)
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return PessoaResponse(id=id, **pessoa.dict())

@router.delete("/pessoas/{id}", status_code=204)
def delete_pessoa(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pessoas WHERE id=?", id)
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return None