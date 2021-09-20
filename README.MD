[![GeoTIFF-Reader App](https://github.com/JARADES-M/GeoTIFF-Reader/actions/workflows/python-app.yml/badge.svg)](https://github.com/JARADES-M/GeoTIFF-Reader/actions/workflows/python-app.yml)
# GeoTIFF Reader

> #### PT-BR Description
A imagem [319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif](images/319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif) é uma imagem de 
satélite multiespectral georreferenciada em formato GeoTIFF obtida pelo 
microssatélite ID 0c0b da constelação PlanetScope em 7 de dezembro de 2016, às 15h19m53s UTC.

Ela possui as seguintes bandas:

ÍNDICE | BANDA | ALCANCE ESPECTRAL (nm)
------ | ----- | -----------------------
1 | Blue | 455 - 515
2 | Green | 500 - 590
3 | Red | 590 - 670
~~5~~ **4** | NIR | 780 - 860

Os seguintes dados serão calculados: 

- Percentual de área desta imagem que está coberto por algum tipo de vegetação
- Centróide geográfico da cena
- Área em quilômetros quadrados da cena
- Data e hora locais (ou seja, em fuso horário local) do local imageado 
  no momento da captura.

Esse cálculo será fornecido através de um endpoint HTTP em formato JSON, desenvolvido usando Python/Flask.
O arquivo [swagger_api.yml](swagger_api.yml) contém a especificação exata do formato de retorno
(incluindo unidades e outros detalhes) e do nome do endpoint. O mesmo pode ser visualizado, também, através do [Swagger Editor](https://editor.swagger.io/).

Nota: O timestamp da captura (em fuso UTC) não está nos cabeçalhos, mas sim no 
próprio nome do arquivo.

### Setup a virtual python environment
```bash
python3 -m venv ~/.geo-tiff-env
```
```bash
source ~/.geo-tiff-env/bin/activate
```

### Build / Run (local)
> Run all steps
```bash
make all
```
> Run only tests
```bash
make test
```
> Run service locally
```bash
python main.py
```
> The service will be available via [localhost:5000/vegetation-cover](http://localhost:5000/vegetation-cover).
> You can also set a value to an env variable named `PORT`, to be the service port number.

### CI/CD

#### **Build** --> **Deploy** (GCP App Engine)

- The build and deploy are triggered automatically when there is a commit or a pull request to the master branch.
- The process will abort with error should an step fail (A failing unit test for example)

> The service is available via this GET endpoint [https://geotiff-reader.uc.r.appspot.com/vegetation-cover](https://geotiff-reader.uc.r.appspot.com/vegetation-cover)

### Deliberations
#### Some of the aspects that were not accounted for when developing the solution are the following:
* Security (Authentication, Authorization, Data Protection, Etc..)
* Performance (Caching or techniques to reduce memory or processing usage for example)
* Project Size (Using the [Google Time Zone API](https://developers.google.com/maps/documentation/timezone/overview#maps_http_timezone_dstoffset-py) instead of importing a lib for example)
* Tests, Unit coverage, Integration
* The complete CI/CD Process and Patterns
* Logs, Monitoring, Alerting, Etc..
* Exception/Error handling
* Versioning (API and libs)
* Containerization - Given that the app is already being deployed in a PaaS

### Learn More:
- [Reading and Visualizing GeoTiff](https://towardsdatascience.com/reading-and-visualizing-geotiff-images-with-python-8dcca7a74510)
- RasterIO Documentation [HTML](https://rasterio.readthedocs.io/en/latest/index.html) | [PDF](https://rasterio.readthedocs.io/_/downloads/en/stable/pdf/)
- [201 - Working with geotiff files using rasterio in python (also quick demo of NDVI calculation)](https://www.youtube.com/watch?v=ieyODuIjXp4)
- [Working with Raster Datasets](https://geohackweek.github.io/raster/04-workingwithrasters/)
- [NDVI Calculation](https://developers.planet.com/tutorials/calculate-ndvi/)
