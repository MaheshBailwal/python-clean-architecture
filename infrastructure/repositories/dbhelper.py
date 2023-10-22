import json
from typing import List, Type, TypeVar
from domain.interfaces.i_product_repo import IProductRepository
from domain.entities.product_ent import ProductEntity
import datetime
import boto3
from boto3.dynamodb.conditions import Key
import os

T = TypeVar("T")

class DBHelper():
   
    def put_item(dic: dict) -> None:
            product_table = DBHelper.get_table()
            now =datetime.datetime.now()
            x = now.strftime("%m/%d/%Y, %H:%M:%S")
            print("8")
            product_table.put_item(Item = dic)
            print("9")
        
    def get_item(key: str):
            product_table = DBHelper.get_table()
            now =datetime.datetime.now()
          
            response = product_table.get_item(
                Key=key
            )
            if 'Item' in response:
                item = response['Item']
                del item['PK']
                del item['SK']
                return item
            else:
                  return None
    
    def query(index : str,key: Key,some_class: Type[T])->List[any]:
            product_table = DBHelper.get_table()
            now =datetime.datetime.now()
                    
            response = product_table.query(
            IndexName=index,
            #KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian') & Key('song').begins_with('C')
            KeyConditionExpression=key,
            )
            result = response['Items']

            while 'LastEvaluateKey' in response:
                response = product_table.query(ExclusiveStartKey=response['LastEvaluatedKey'])
                result.extend(response['Items'])

            items = response['Items']
            list_enty = list()

            for item in items:
                del item['PK']
                del item['SK']
                enty= some_class(item)
                list_enty.append(enty)

            return list_enty

    def get_table():
        dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'ap-south-1',
                aws_access_key_id = '',
                aws_secret_access_key = '')

            ### getting the product table
        product_table = dynamo_client.Table('product')
        product_table.table_status
        
        return product_table
