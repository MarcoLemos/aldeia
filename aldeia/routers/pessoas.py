from typing import List

from fastapi import APIRouter, HTTPException
from odmantic import ObjectId

from ..main import engine
from ..models import Pessoas

router = APIRouter(
    prefix='/pessoas',
    tags=['pessoas'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/', response_model=List[Pessoas])
async def get_pessoas():
    pessoas = await engine.find(Pessoas)
    return pessoas


@router.get('/count', response_model=int)
async def count_pessoas():
    count = await engine.count(Pessoas)
    return count


@router.get('/{id}', response_model=Pessoas)
async def get_pessoa_by_id(id: ObjectId):
    pessoa = await engine.find_one(Pessoas, Pessoas.id == id)
    if pessoa is None:
        raise HTTPException(404)
    return pessoa


@router.post('/', response_model=Pessoas)
async def create_pessoa(pessoas: Pessoas):
    await engine.save(pessoas)
    return pessoas


@router.delete('/{id}', response_model=Pessoas)
async def delete_pessoa_by_id(id: ObjectId):
    pessoa = await engine.find_one(Pessoas, Pessoas.id == id)
    if pessoa is None:
        raise HTTPException(404)
    await engine.delete(pessoa)
    return pessoa
