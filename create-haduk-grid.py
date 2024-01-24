import os
import json
import fsspec
import kerchunk.hdf, kerchunk.netCDF3
from kerchunk.combine import MultiZarrToZarr
import glob

pattern = "/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.2.0.ceda/1km/tas/ann/v20230328/tas_hadukgrid_uk_1km_ann_*.nc"

def fix(content):
    del content["refs"]["time_bnds/.zarray"]
    del content["refs"]["time_bnds/.zattrs"]
    del content["refs"]["time_bnds/0.0"]
    content["refs"]["time/.zattrs"] = content["refs"]["time/.zattrs"].replace('\n    "bounds": "time_bnds",', "")


def main():
    output_uri = "/home/users/astephen/climate-stripes/pystripes/haduk-grid1.json"
    file_uris = glob.glob(pattern)
    single_indexes = []

    #file_uris = file_uris[:3]
    print(f"Scanning: {len(file_uris)} files")

    for file_uri in file_uris:
        print(f"[INFO] Processing: {file_uri}")
        indx = kerchunk.hdf.SingleHdf5ToZarr(file_uri, inline_threshold=100000).translate()
#        fix(indx)
        
        single_indexes.append(indx)

    kwargs = {
        "coo_map": {"time": "cf:time"}, 
        "identical_dims": ["projection_y_coordinate", "projection_x_coordinate", "latitude", "longitude"], 
        "concat_dims": ["time"]
    }

    mzz = MultiZarrToZarr(single_indexes, **kwargs) 
    json_content = mzz.translate() 

    with fsspec.open(output_uri, "wb", compression=None) as kc_file:
        kc_file.write(json.dumps(json_content).encode())

    print(f"[INFO] Written file: {output_uri}")


main()
