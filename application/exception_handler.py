import traceback
from aws_lambda_powertools.event_handler import Response,content_types

def exception_response (ex: Exception): 
    exName = ex.__class__.__name__
    status_code=500
    tb = traceback.format_exc()
    match exName:
        case "ValidationError":
            status_code=400
        case "RescourceNotFoundException":
            status_code=404
        case "AlreadyExistException":
            status_code=409
  
    return Response(
        status_code=status_code,
        content_type=content_types.TEXT_PLAIN,
        body=str(ex) + tb,
    )
