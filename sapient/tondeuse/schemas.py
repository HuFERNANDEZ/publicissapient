from typing import List, Optional
from typing_extensions import Literal

from datetime import date
from enum import Enum

from pydantic import BaseModel


class Mower(BaseModel):
    id: str
    capacity: float
    failure_rate: float
    margin: float
    price: float
    prod_cost: float
    product_type: Literal["auto-portee", "essence", "electrique"]
    quality: Literal["Low", "Medium", "Hight"]
    warranty: str

class MowerAttractiveness(Mower):
    attractiveness: float
