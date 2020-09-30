import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
import numpy as np
import folium
from PIL import Image
from folium.plugins import HeatMap
df = pd.read_csv('/content/drive/My Drive/project/EARTHQUAKE VISUALIZATION/Earthquake.csv')#please select the path for Earthquake.csv
x = np.array(df[['longitude','latitude', 'mag']], dtype='float64')
plt.scatter(x[:,0], x[:,1], alpha=0.2, s= 50)
plt.show()
m = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=5)
for _, row in df.iterrows():
  if row.mag >= 5:
    folium.CircleMarker(
        location=[row.latitude, row.longitude],
        radius=5,
        popup=re.sub(r'[^a-zA-Z]+', '', row.time),
        color='#FE1A16',
        fill=True,
        fill_colour='#FE1A16'
    ).add_to(m)
  else:
    folium.CircleMarker(
        location=[row.latitude, row.longitude],
        radius=5,
        popup=re.sub(r'[^a-zA-Z]+', '', row.time),
        color='#ffbd87',
        fill=True,
        fill_colour='#ffbd87'
    ).add_to(m)
m.save("scattered_plot.png")
im = Image.open("scattered_plot.png")
im.show()
m1=folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=5)
HeatMap(data=df[['latitude', 'longitude', 'mag']].groupby(['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(m1)
m1.save("HeatMap.png")
im1 = Image.open("scattered_plot.png")
im1.show()