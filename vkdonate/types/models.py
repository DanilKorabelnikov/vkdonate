from pydantic import BaseModel

from typing import List

class DonatesModel(BaseModel):
    uid: int = None

class Model(BaseModel):
    count: int = None
    donates: List[DonatesModel] = None