from typing import List, Optional
from bson import ObjectId

from app.models import Route
from app.db import db


class RouteRepository:
    collection = db.routes

    @staticmethod
    async def create_route(start: str, end: str, waypoints: list[str]) -> Route:
        doc = {"start_point": start, "end_point": end, "waypoints": waypoints}
        result = await RouteRepository.collection.insert_one(doc)
        return Route(route_id=str(result.inserted_id), start_point=start, end_point=end, waypoints=waypoints)

    @staticmethod
    async def get_route_by_id(route_id: str) -> Optional[Route]:
        doc = await RouteRepository.collection.find_one({"_id": ObjectId(route_id)})
        if not doc:
            return None
        return Route(
            route_id=str(doc["_id"]),
            start_point=doc["start_point"],
            end_point=doc["end_point"],
            waypoints=doc.get("waypoints", [])
        )

    @staticmethod
    async def get_all_routes() -> List[Route]:
        routes: List[Route] = []
        async for doc in RouteRepository.collection.find():
            routes.append(
                Route(
                    route_id=str(doc["_id"]),
                    start_point=doc["start_point"],
                    end_point=doc["end_point"],
                    waypoints=doc.get("waypoints", [])
                )
            )
        return routes
