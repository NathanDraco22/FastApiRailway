from fastapi import FastAPI
from .routers import ws_router
from .routers.gql_router import graphQLAPP

app : FastAPI = FastAPI()

app.include_router( prefix= "/ws" ,router= ws_router.websocket_router )
app.include_router( prefix= "/gql",router=  graphQLAPP)

