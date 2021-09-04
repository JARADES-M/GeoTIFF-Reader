from flask import (
    Flask, 
    jsonify
)
from services import image_processor

app = Flask(__name__)

@app.route('/vegetation-cover', methods=['GET'])
def get_vegetation_cover():
    """
    Desc.
    """
    #TODO
    cover_info = image_processor.get_default_image_info()
    return jsonify(cover_info.getInfo())

if __name__ == '__main__':
    app.run(debug=True)