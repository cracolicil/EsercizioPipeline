from pydantic import BaseModel, Field

class CountResult(BaseModel):
    total: int
    letters: int
    numbers: int
    spaces: int
    punctuation: int