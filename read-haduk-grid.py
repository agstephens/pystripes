import xarray as xr
import fsspec

def get_dataset(index_uri):

    compression = "zstd" if index_uri.split(".")[-1].startswith("zst") else None
    mapper = fsspec.get_mapper("reference://", fo=index_uri, target_options={"compression": compression})
    ds = xr.open_zarr(mapper, consolidated=False, use_cftime=True, decode_timedelta=False)
    return ds


fpath = "/home/users/astephen/climate-stripes/pystripes/haduk-grid1.json"
ds = get_dataset(fpath)

print(ds)
print(ds.time)
print("lat shape", ds.latitude.shape)
