from fastapi import APIRouter, HTTPException
from .. import crud

router = APIRouter(prefix="/count")