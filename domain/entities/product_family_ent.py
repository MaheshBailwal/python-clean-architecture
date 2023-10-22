from ast import List
import json
from uuid import UUID
from domain.custom_encoder import CustomeEncoder
from domain.dtos.product_family_dtos import *

class ProductFamilyEntity():
    family_id:str
    description:str
    entity:str
    is_active:bool
  
    def __init__(self,prop_dict=None):
        if prop_dict != None:
            self.__dict__ = prop_dict
    
    def to_dto(self)->ProductFamilyDetailDto:
        dto = ProductFamilyDetailDto()
        dto.family_id = self.family_id
        dto.description = self.description
        dto.is_active = self.is_active
        return dto
    
    def set(self, dto:ProductFamilySetDto):
        self.family_id = dto.family_id
        self.description = dto.description
        self.is_active = dto.is_active
        return self
