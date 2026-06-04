from fastapi import APIRouter, HTTPException
from .. import crud
from ..models import CountResult, TextToCount
import datetime

router = APIRouter(prefix="/count")

@router.post("", response_model=CountResult)
def count_each_type(text: TextToCount):
    start_dt = datetime.datetime.now()
    result = crud.count_each_type(text.model_dump()["text"])
    end_dt = datetime.datetime.now()
    difference = (end_dt - start_dt).total_seconds()
    print(f"Secondi: {difference*1000}")
    return result