class Centroid:
    def __init__(self, type: str, coordinates: "list[float]"):

        self.type = type
        self.coordinates = coordinates

    def toObject(self) -> "dict[str, Any]":

        return {"type": self.type, "coordinates": self.coordinates}
