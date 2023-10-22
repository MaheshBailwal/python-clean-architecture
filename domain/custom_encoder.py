import json

from domain.dtos.product_dtos import *

class CustomeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ConstraintDto):
            return obj.__dict__
        
        return json.JSONEncoder.default(self,obj)
