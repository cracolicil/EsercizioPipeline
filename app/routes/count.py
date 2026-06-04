from fastapi import APIRouter, HTTPException
from .. import crud
from ..models import CountResult, TextToCount

router = APIRouter(prefix="/count")

@router.post("")
def count_each_type(text: TextToCount):
    return crud.count_each_type(text.model_dump()["text"])