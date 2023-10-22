
from dataclasses import asdict, is_dataclass
import json
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from application.response_builder import ResponseBuilder
from domain.dtos.product_dtos import *
from domain.services.product_srv import *
from infrastructure.repositories.product_repo import ProductRepository
from aws_lambda_powertools.event_handler.api_gateway import Router


tracer = Tracer()
logger = Logger()
router = Router()
repo = ProductRepository()
ps = ProductService(repo)

@router.post("/")
@tracer.capture_method
def create_product():
    parsed_payload: ProductSetDto = parse(event=router.current_event.body, model=ProductSetDto)
    ps.set(parsed_payload)
    return ResponseBuilder.build(parsed_payload.product)

@router.get("/")
@tracer.capture_method
def get_all():
    dtos = ps.get_all()
    return ResponseBuilder.build(dtos)

@router.get("/<productId>")
@tracer.capture_method
def get_product(productId:str):
    dto = ps.get(productId)
    return   ResponseBuilder.build(dto)
    

