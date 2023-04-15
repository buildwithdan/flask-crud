from serverless_wsgi import handle_request
from app import application

def wsgi_handler(event, context):
    return handle_request(application, event, context)
