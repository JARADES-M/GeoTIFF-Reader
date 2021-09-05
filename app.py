import os
from services import image_processor
from flask import (
    Flask, 
    jsonify
)

PORT = 5000 if os.getenv('PORT') is None else os.getenv('PORT')

app = Flask(__name__)

@app.route('/vegetation-cover', methods=['GET'])
def get_vegetation_cover():
    """
    Get information about an specific GeoTIFF file.
    """

    cover_info = image_processor.get_default_image_info()
    return jsonify(cover_info.getInfo())

if __name__ == '__main__':
    app.run(debug=True, port=PORT)