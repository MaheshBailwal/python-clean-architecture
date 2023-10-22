
from ast import List
from aws_lambda_powertools.utilities.parser import parse, BaseModel, ValidationError
from dataclasses import dataclass
from typing import List, Optional


class ProductFamilyDetailDto:
        family_id:str
        description:str
        is_active:bool
 
class ProductFamilySetDto(BaseModel):
        family_id:Optional[str]
        description:str
        is_active:bool

