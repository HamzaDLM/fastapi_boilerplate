from fastapi import APIRouter

from api.api_v1.endpoints import endpoint1, endpoint2, loghandler


api_router = APIRouter()


api_router.include_router(endpoint1.router,
                          prefix="/endpoint1",
                          tags=["endpoint1"])

api_router.include_router(endpoint2.router,
                          prefix="/endpoint2",
                          tags=["endpoint2"])

api_router.include_router(loghandler.router,
                          prefix="/loghandler",
                          tags=["loghandler"])
