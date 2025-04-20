from typing import List, Optional
from app.models import Route
from app.repositories.route_repository import RouteRepository


class RouteService:
    """
    Бизнес-логика для маршрутов.
    Тут можно взаимодействовать с внешними сервисами:
    (например, вызов MapService для расчёта расстояния и т.д.)
    """

    def __init__(self, repo: RouteRepository):
        self.repo = repo

    def create_new_route(self, start: str, end: str, waypoints: list[str]) -> Route:
        # Здесь можно вызвать MapService, посмотреть расстояние и т.п.
        # Пока что просто создаём
        return self.repo.create_route(start, end, waypoints)

    def get_route(self, route_id: int) -> Optional[Route]:
        return self.repo.get_route_by_id(route_id)

    def list_routes(self) -> List[Route]:
        return self.repo.get_all_routes()
