import logging

from fastapi import APIRouter, Request
api = APIRouter()


logger = logging.getLogger(__name__)

@api.get("/collections")
def collections(request: Request):
    body = request.json()
    return({"test":'blabla'})
