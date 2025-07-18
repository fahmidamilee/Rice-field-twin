
import elevation
import rasterio
import matplotlib.pyplot as plt

lat, lon = 10.5, 105.3
bounds = (lon - 0.02, lat - 0.02, lon + 0.02, lat + 0.02)

# Download DEM
elevation.clip(bounds=bounds, output='dem.tif')

# Read DEM
with rasterio.open('dem.tif') as src:
    dem = src.read(1)
    plt.imshow(dem, cmap='terrain')
    plt.colorbar(label='Elevation (m)')
    plt.title('Rice Field Terrain (DEM)')
    plt.show()
