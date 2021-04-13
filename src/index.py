import tkinter as tk
import geopandas as gdp
import pandas as pd
import os
import json


def main():
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


if __name__ == '__main__':
  main()