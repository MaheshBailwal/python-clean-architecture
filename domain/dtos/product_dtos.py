
from ast import List
from aws_lambda_powertools.utilities.parser import parse, BaseModel, ValidationError
from dataclasses import dataclass
from typing import List, Optional

class ConstraintDto(BaseModel):
        attribute:str
        op :str
        value:int

class ProductDetailDto:
        product:str
        description:str
        family:str
        packaging:str
        services : List[str]
        constraints: List[ConstraintDto]
        restricted: bool
 
class ProductSetDto(BaseModel):
        product:str
        description:Optional[str]
        family:str
        packaging:str
        services :List[str]
        constraints:Optional[List[ConstraintDto]]
        restricted: bool

