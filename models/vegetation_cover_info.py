from typing import Any
from models.centroid import Centroid


class VegetationCoverInfo:
    def __init__(
        self,
        filename: str,
        cover: float,
        area: float,
        centroid: Centroid,
        local_datetime: str,
    ):

        self.filename = filename
        self.cover = cover
        self.area = area
        self.centroid = centroid
        self.local_datetime = local_datetime[0]

    def toObject(self) -> "dict[str, Any]":

        return {
            "filename": self.filename,
            "cover": self.cover,
            "area": self.area,
            "centroid": self.centroid.toObject(),
            "local_time": self.local_datetime,
        }
