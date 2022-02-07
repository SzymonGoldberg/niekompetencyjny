import json
from RoomTemplate import RoomTemplate
from figures import Point, Rect


class JsonIO:
    @staticmethod
    def read(filepath: str) -> list:
        assert len(filepath)
        rooms = []
        with open(filepath, "r") as f:
            loaded = json.load(f)
            for v in loaded["rooms"]:
                room = RoomTemplate(
                    v["name"], v["minSize"][0], v["minSize"][1], v["expandable"]
                )
                for neighbour in v["neighbors"]:
                    room.addNeighbourString(neighbour)
                room.exit = v["exit"] if v.get("exit") else False
                rooms.append(room)
            area = Rect(Point.zero(), loaded["area"][0], loaded["area"][1])
            return area, rooms