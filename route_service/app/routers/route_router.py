from typing import List
from fastapi import APIRouter, Depends, HTTPException

from app.schemas import RouteCreateRequest, RouteResponse
from app.services.route_service import RouteService
from app.repositories.route_repository import RouteRepository
from app.auth import verify_token

router = APIRouter(prefix="/routes", tags=["routes"])

route_service = RouteService(repo=RouteRepository())


@router.post("", response_model=RouteResponse, dependencies=[Depends(verify_token)])
def create_route(data: RouteCreateRequest):
    """
    Создать новый маршрут
    """
    route = route_service.create_new_route(
        start=data.start_point, end=data.end_point, waypoints=data.waypoints or []
    )
    return route.dict()


@router.get("/{route_id}", response_model=RouteResponse, dependencies=[Depends(verify_token)])
def get_route_by_id(route_id: int):
    """
    Получить маршрут по его ID
    """
    route = route_service.get_route(route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route.dict()


@router.get("", response_model=List[RouteResponse], dependencies=[Depends(verify_token)])
def list_all_routes():
    """
    Получить список всех маршрутов
    """
    routes = route_service.list_routes()
    return [r.dict() for r in routes]
