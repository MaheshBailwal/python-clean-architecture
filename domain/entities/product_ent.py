from ast import List
import json
from uuid import UUID
from domain.custom_encoder import CustomeEncoder
from domain.dtos.product_dtos import *

class ProductEntity():
    product:str
    description:str
    family:str
    packaging:str
    services=[]
    constraints:[]
    restricted: bool

    def __init__(self,prop_dict=None):
        if prop_dict != None:
            self.__dict__ = prop_dict
    
    def to_dto(self)->ProductDetailDto:
        dto = ProductDetailDto()
        dto.product = self.product
        dto.description = self.description
        dto.family = self.family
        dto.packaging = self.packaging
        dto.services = self.services
        dto.constraints = self.constraints
        dto.restricted = self.restricted
        return dto
    
    def set(self, dto:ProductSetDto):
        self.product = dto.product
        self.description = dto.description
        self.family = dto.family
        self.packaging = dto.packaging
        self.services = dto.services
        cn =json.dumps(dto.constraints, separators=(",", ":"), cls=CustomeEncoder)
        self.constraints =  cn
        self.restricted = dto.restricted
        return self
