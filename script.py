import geopandas
import cartopy.crs as crs
from pathlib import Path
import matplotlib.pyplot as plt


# Site: https://www.naturalearthdata.com/downloads/
# Download: https://naciscdn.org/naturalearth/packages/natural_earth_vector.zip
fp = Path("../natural_earth_vector/50m_cultural")
bound_fp = fp / ("ne_50m_admin_0_boundary_lines_land.shp")
country_fp = fp / ("ne_50m_admin_0_countries.shp")

bounds = geopandas.read_file(bound_fp)
countries = geopandas.read_file(country_fp)

north_pole_crs = crs.AzimuthalEquidistant(central_latitude=90, central_longitude=90)
bounds = bounds.to_crs(north_pole_crs)
countries = countries.to_crs(north_pole_crs)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=north_pole_crs)

bounds.plot(ax=ax, color="black")
countries.plot(ax=ax, color="blue")

gl = ax.gridlines(crs=crs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')

plt.show()