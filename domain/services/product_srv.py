from  domain.entities.product_ent import ProductEntity
from domain.dtos.product_dtos import *
from domain.exceptions.not_found_exce import RescourceNotFoundException
from domain.interfaces.i_product_repo import IProductRepository

class ProductService:
    def __init__(self, repo: IProductRepository):
        self.repo = repo
 
    def set(self, dto: ProductSetDto)->None:
        pe = ProductEntity()
        pe.set(dto)
        self.repo.save(pe)

    def get(self, product_id: str)->ProductDetailDto:
       enty = self.repo.get_by_id(product_id)
       if enty is None:raise RescourceNotFoundException(f"product {product_id} not found")
       return enty.to_dto()
    
    def get_all(self)->list[ProductDetailDto]:
       list_dto = list()
       entities = self.repo.get_all()
       for enty in entities:
          try:
            list_dto .append(enty.to_dto())
          except:
           pass
       return list_dto
 