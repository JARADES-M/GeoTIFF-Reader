import os
from flask import Flask
from flask_restful import Resource, Api
from services import image_processor

PORT = 5000 if os.getenv("PORT") is None else os.getenv("PORT")

app = Flask(__name__)
api = Api(app)


class VegetarionCover(Resource):
    def get(self):
        """
        Get information about an specific GeoTIFF file.
        """
        cover_info = image_processor.get_default_image_info()
        return cover_info.toObject(), 200


api.add_resource(VegetarionCover, "/vegetation-cover")

if __name__ == "__main__":
    app.run(debug=True, port=PORT)
