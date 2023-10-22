import json

from domain.dtos.product_dtos import *
from domain.dtos.product_family_dtos import *

class ResponseEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ProductDetailDto):
            return obj.__dict__
        if isinstance(obj, ConstraintDto):
            return obj.__dict__
        if isinstance(obj, ProductFamilyDetailDto):
            return obj.__dict__
        
        return json.JSONEncoder.default(self,obj)

def custom_serializer(obj) -> str:
    """Your custom serializer function APIGatewayRestResolver will use"""
    return json.dumps(obj, separators=(",", ":"), cls=ResponseEncoder)