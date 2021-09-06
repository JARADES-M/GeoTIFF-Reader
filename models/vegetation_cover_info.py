from typing import Any
from models.centroid import Centroid


class VegetationCoverInfo:
    def __init__(
        self,
        file_name: str,
        cover: float,
        area: float,
        centroid: Centroid,
        local_time: str,
    ):

        self.file_name = file_name
        self.cover = cover
        self.area = area
        self.centroid = centroid
        self.local_time = local_time[0]

    def toObject(self) -> "dict[str, Any]":

        return {
            "filename": self.file_name,
            "cover": self.cover,
            "area": self.area,
            "centroid": self.centroid.toObject(),
            "local_time": self.local_time,
        }
