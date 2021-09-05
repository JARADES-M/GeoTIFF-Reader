from models.centroid import Centroid
from models.vegetation_cover_info import VegetationCoverInfo
import rasterio as rio
import numpy as np
from datetime import datetime
from dateutil import tz
from timezonefinder import TimezoneFinder

DEFAULT_IMAGE_PATH = r"./images/319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif"
TZF = TimezoneFinder()

def get_default_image_info() -> VegetationCoverInfo:

    with rio.open(DEFAULT_IMAGE_PATH) as dataset:

        coordinates=dataset.lnglat()
        centroid = Centroid(type="Point", coordinates=coordinates)

        width = dataset.bounds[2] - dataset.bounds[0]
        height = dataset.bounds[3] - dataset.bounds[1]

        ndvi = get_ndvi_from_dataset(dataset=dataset)

        local_time=get_local_datetime_from_filename(
            filename=dataset.name, lng=coordinates[0], lat=coordinates[1]),

        return VegetationCoverInfo(
            file_name=dataset.name,
            cover=(ndvi.sum() / ndvi.size),
            centroid=centroid,
            area=(width * height),
            local_time=local_time,
        )


def get_ndvi_from_dataset(dataset) -> float:

    red = dataset.read(3).astype("float64")
    nir = dataset.read(4).astype("float64")
    np.seterr(divide="ignore", invalid="ignore")
    return np.where((nir + red) == 0.0, 0, (nir - red) / (nir + red))


def get_local_datetime_from_filename(filename: str, lng: float, lat: float) -> str:

    to_zone =  tz.gettz(get_timezone_from_lng_lat(lng, lat))
    str_utc = filename.split("-")[-1].split(".")[0]
    utc = datetime.strptime(str_utc, "%Y%m%dT%H%M%SZ")
    return utc.astimezone(to_zone).isoformat()


def get_timezone_from_lng_lat(lng: float, lat: float) -> str:
    return TZF.timezone_at(lng=lng, lat=lat)


if __name__ == "__main__":
    get_default_image_info()
