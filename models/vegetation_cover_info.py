class VegetationCoverInfo:

    def __init__(self, file_name, cover, area, centroid, local_time):
        self.file_name = file_name
        self.cover = cover
        self.area = area
        self.centroid = centroid
        self.local_time = local_time

    def getInfo(self):
        
        return {
            "filename": self.file_name,
            "cover": self.cover,
            "area": self.area,
            "centroid": self.centroid,
            "local_time": self.local_time
        }