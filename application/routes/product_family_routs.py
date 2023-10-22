
from dataclasses import asdict, is_dataclass
import json
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from application.response_builder import ResponseBuilder
from domain.dtos.product_family_dtos import *
from domain.services.product_family_srv import *
from infrastructure.repositories.product_family_repo import ProductFamilyRepository
from aws_lambda_powertools.event_handler.api_gateway import Router


tracer = Tracer()
logger = Logger()
router = Router()
repo = ProductFamilyRepository()
service = ProductFamilyService(repo)

@router.put("/")
@tracer.capture_method
def create_product():
    parsed_payload: ProductFamilySetDto = parse(event=router.current_event.body, model=ProductFamilySetDto)
    service.set(parsed_payload)
    return ResponseBuilder.build(parsed_payload.family_id)

@router.get("/")
@tracer.capture_method
def get_all():
    dtos = service.get_all()
    return ResponseBuilder.build(dtos)

@router.get("/<familyId>")
@tracer.capture_method
def get_product(familyId:str):
    dto = service.get(familyId)
    return   ResponseBuilder.build(dto)
    

