print("imports")
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

import xarray as xr
import fsspec
from convertbng.util import convert_bng

import sys
sys.path.insert(0, ".")
from colours import colmap as colour_list

print("setup")
cols =  np.array(colour_list[0] + [colour_list[1]] + colour_list[2]) / 255
N = 100
cmap = LinearSegmentedColormap.from_list("warming_strips_red_blue", cols, N=N)

random_data = np.array([i + (random.randint(-5, 5)) for i in range(N)])
#random_mesh = np.vstack(random_data * N).T

RAL_COORDS = [51.570664384, -1.308832098]
EXMOUTH_COORDS = [50.6200, -3.4137]
fpath = index_uri = "haduk-grid1.json"


def lat_lon_to_northings_eastings(lat, lon):
    eastings, northings = convert_bng(lon, lat)
    return northings[0], eastings[0]


def get_data(lat, lon, ref_period=["1971", "2000"]):
    compression = "zstd" if index_uri.split(".")[-1].startswith("zst") else None
    mapper = fsspec.get_mapper("reference://", fo=index_uri, target_options={"compression": compression})

    print("opening kerchunk...need bigger arrays and specify duplicate coords and lat lon from each")
    ds = xr.open_zarr(mapper, consolidated=False, use_cftime=True, decode_timedelta=False)

    print("convert to northings, eastings...")
    northings, eastings = lat_lon_to_northings_eastings(lat, lon)
 
    print("extract nearest grid point...")
    data = ds.tas.sel(projection_y_coordinate=northings, projection_x_coordinate=eastings, method="nearest")
    lats = ds.latitude
    lons = ds.longitude

    y, x = float(data.projection_y_coordinate.values), float(data.projection_x_coordinate.values)
    print(f"location check: {float(lats.sel(projection_y_coordinate=y, projection_x_coordinate=x))},")
    print(f"                {float(lons.sel(projection_y_coordinate=y, projection_x_coordinate=x))}")

    # Subtract reference period
    ref_mean = data.sel(time=slice(*ref_period)).mean()
    data = (data.sel(time=slice("1901", "2000")) - ref_mean).squeeze().to_series()
    return data
    

def plot1(data=random_data, n=N):
    data = np.array(list(data[:N]))
    data = np.vstack(data * N).T 

    plt.pcolormesh(data, cmap=cmap, rasterized=True) #, vmin=-4, vmax=4)
    #plt.show()
    png = "stripes.png"
    plt.savefig(png)
    print(f"Wrote: {png}")


def main(lat, lon):
    print("data")
    data = get_data(lat, lon)
    print("plot")
    plot1(data)
    print("done")


if __name__ == "__main__":

    lat, lon = [float(i) for i in sys.argv[1:3]]
#main(*RAL_COORDS)
#main(*EXMOUTH_COORDS)
    main(lat, lon)

