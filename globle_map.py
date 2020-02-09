import geopandas as gpd
from pyproj import CRS
import matplotlib.pyplot as plt
fp = r"E:\study_cailiao\py_study\L2_data\ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp"
admin = gpd.read_file(fp)
ortho = CRS.from_proj4('+proj=ortho +lat_0=22.32 +lon_0=114.03 +x_0=0 +y_0=0 +a=6370997 +b=6370997 +units=m +no_defs')
admin.to_crs(ortho).plot()
plt.axis('off')
plt.title("Orthographic")
plt.show()

hallo fangfei