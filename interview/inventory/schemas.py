
from decimal import Decimal
from pydantic import BaseModel
from typing import List


class InventoryMetaData(BaseModel):
    year: int
    actors: List[str]
    imdb_rating: Decimal
    rotten_tomatoes_rating: int