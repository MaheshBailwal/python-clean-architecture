import json
from uuid import uuid4
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from application.exception_handler import exception_response
from application.routes import product_family_routs,product_routs
from application.response_encoder import *


tracer = Tracer()
logger = Logger()
app = APIGatewayHttpResolver(serializer=custom_serializer)
app.include_router(product_routs.router,prefix="/product")
app.include_router(product_family_routs.router,prefix="/productFamily")

@app.exception_handler(Exception)
def handle_error(ex: Exception):  
    metadata = {"path": app.current_event.path, "query_strings": app.current_event.query_string_parameters}
    exName = ex.__class__.__name__
    logger.error(f"error_type: {exName} message: {ex}", extra=metadata)
    return exception_response(ex)

def lambda_handler(event: dict, context: LambdaContext)->any:
        res= app.resolve(event, context)
        body = res["body"]
        body = body.replace('\\', '')
        body = body.replace('"[', '[')
        body = body.replace(']"', ']')
        res["body"]=body
        return res 
   