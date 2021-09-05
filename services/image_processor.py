from models.vegetation_cover_info import VegetationCoverInfo
import rasterio as rio
import numpy as np

DEFAULT_IMAGE_PATH = r'./images/319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif'

def get_default_image_info():

    with rio.open(DEFAULT_IMAGE_PATH) as dataset:

        centroid = {"type":"Point", "coordinates": [dataset.lnglat()]}

        width = dataset.bounds[2] - dataset.bounds[0]
        height = dataset.bounds[3] - dataset.bounds[1]

        ndvi = get_ndvi_from_dataset(dataset=dataset)

        return VegetationCoverInfo(
            file_name=dataset.name,
            cover=(ndvi.sum() / ndvi.size),
            centroid=centroid,
            #area=(dataset.width * dataset.height), TODO check
            area=(width * height),
            local_time=""
            )

def get_ndvi_from_dataset(dataset):

    red = dataset.read(3).astype('float64')
    nir = dataset.read(4).astype('float64')
    np.seterr(divide='ignore', invalid='ignore')
    return np.where((nir+red)==0., 0, (nir-red)/(nir+red))

def get_local_datetime_from_filename(filename):
    #TODO
    pass


if __name__ == '__main__':
    get_default_image_info()