from uuid import uuid4
import uuid
from domain.exceptions.already_exist_exce import AlreadyExistException
from domain.interfaces.i_product_family_repo import IProductFamilyRepository
from domain.entities.product_family_ent import ProductFamilyEntity
from boto3.dynamodb.conditions import Key

from infrastructure.repositories.dbhelper import DBHelper

class ProductFamilyRepository(IProductFamilyRepository):
   
    def save(self, enty: ProductFamilyEntity) -> None:
            dic = enty.__dict__
            dic['PK'] = "PF#"+ enty.family_id
            dic['SK'] = "#PF#" + str()
            dic['entity'] = "productfamily"
            dic['unique_description'] = "#PF#" + enty.description.upper()
            
            if self.exits(enty):
              raise AlreadyExistException(f"product family {enty.description} alteary exists")
           
            DBHelper.put_item(dic)
        
    def get_by_id(self, family_id: str) -> ProductFamilyEntity:
            key =  Key={
                    "PK": "PF#"+family_id,
                    "SK": "#PF#"
                }
            item = DBHelper.get_item(key)
            if item is None:
                   return None
            enty = ProductFamilyEntity(item)
            return enty
    
    def get_all(self) -> list[ProductFamilyEntity]:
         k=Key('SK').eq('#PF#')
         return DBHelper.query('SK-PK-index',k,ProductFamilyEntity)
    
    def exits(self, enty: ProductFamilyEntity) -> bool:
         k= Key('unique_description').eq('#PF#'+ enty.description.upper()) 
         items = DBHelper.query('unique_description-index',k,ProductFamilyEntity)
        
         if len(items) == 1 and items[0].family_id != enty.family_id:
            return True
       

         if len(items) > 1:
            return True
         
         return False
       

        
  