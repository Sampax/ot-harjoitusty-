import tkinter as tk
import geopandas as gdp
import os
import json

import pandas as pd

from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer



dir = os.path.dirname(__file__)
shapefile = os.path.join(dir, 'data/shapes/ne_110m_admin_0_countries.shp')
datafile = os.path.join(dir, 'data/happiness/happiness-cantril-ladder.csv')

#Read shapefile using Geopandas
gdf = gdp.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
#Rename columns.
gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()

#Read data file
df = pd.read_csv(datafile)
df.head()

#Filter data for year 2018
df_2018 = df[df['Year'] == 2018]
merged = gdf.merge(df_2018, left_on = 'country_code', right_on = 'Code')

#convert to json for bokkeh
gdf_json = json.loads(merged.to_json())
json_data = json.dumps(gdf_json)



# Render in bokeh
geosource = GeoJSONDataSource(geojson = json_data)

palette = brewer['YlGnBu'][4]
palette = palette[::1]

color_mapper = LinearColorMapper(palette = palette, low = 0, high = 10)

p = figure(
  title = 'The world',
  plot_height = 600,
  plot_width = 950,
  toolbar_location = None
)

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

p.patches(
  'xs',
  'ys',
  source = geosource,
  fill_color = {
    'field':'Life satisfaction in Cantril Ladder (World Happiness Report 2019)',
    'transform': color_mapper
  },
  line_color = 'black',
  line_width = 0.25,
  fill_alpha = 1
)

output_notebook()
show(p)
