import json
from domain.interfaces.i_product_repo import IProductRepository
from domain.entities.product_ent import ProductEntity
from boto3.dynamodb.conditions import Key
import datetime
import boto3
import os

from infrastructure.repositories.dbhelper import DBHelper

class ProductRepository(IProductRepository):
   
    def save(self, product: ProductEntity) -> None:
            dic = product.__dict__
            dic['PK'] = "PR#"+ str(product.product.upper().replace(' ','_'))
            dic['SK'] = "#PR#" + str()
            DBHelper.put_item(dic)
        
    def get_by_id(self, product_id: str) -> ProductEntity:
            key =  Key={
                    "PK": "PR#"+product_id,
                    "SK": "#PR#"
                }
            item = DBHelper.get_item(key)
            if item is None:
                   return None
            product_ent = ProductEntity(item)
            return product_ent
    
    def get_all(self) -> list[ProductEntity]:
         k=Key('SK').eq('#PR#')
         return DBHelper.query('SK-PK-index',k,ProductEntity)

        
  