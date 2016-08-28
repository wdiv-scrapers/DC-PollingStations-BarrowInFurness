from geojson_scraper import scrape


stations_url = "https://webgis1.barrowbc.gov.uk/inspire/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=BBC%3APOLLINGSTATIONS&outputFormat=json&srsName=EPSG%3A4326"
districts_url = "https://webgis1.barrowbc.gov.uk/inspire/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=BBC%3ACURRENTPOLLINGDISTRICTS&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'E07000027'


scrape(stations_url, council_id, 'utf-8', 'stations')
scrape(districts_url, council_id, 'utf-8', 'districts')
