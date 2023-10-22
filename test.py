import json
from uuid import uuid4
from application.response_encoder import ResponseEncoder
from domain.dtos.product_dtos import ConstraintDto
from boto3.dynamodb.conditions import Key
from domain.services.product_srv import ProductService

from infrastructure.repositories.product_repo import ProductRepository



def test():
    repo = ProductRepository()
    ps = ProductService(repo)
    objs = ps.get_all()


    pp = json.dumps(objs,cls=ResponseEncoder)
    print(pp)
   
test()

