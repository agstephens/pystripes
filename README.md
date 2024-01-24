# pystripes

Climate stripes python library


## Running the code

If everything is set up, you can run with:

For RAL lat and lon:

```
python make-stripes.py 51.570664384 -1.308832098
```

For Exmouth:

```
python make-stripes.py 50.6200 -3.4137
```

Output file is stripes file: `stripes.png`

## Kerchunk creation

See: /home/users/astephen/kerchunk-intake/eodh-sandbox

## Data sources

From Ed:

https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/England.txt

The UK data comes from the Met Office, specifically this page: https://www.metoffice.gov.uk/research/climate/map
s-and-data/uk-and-regional-series
which produces links to text files like this one for England: https://www.metoffice.gov.uk/pub/data/weather/uk/c
limate/datasets/Tmean/date/England.txt

Ed reads the files for various countries/regions and use the plotshowstripes code to make the graphics.

### Or use 1km HadUK-Grid

/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.2.0.ceda/1km/tas/ann/v20230328

## Running from scratch on JASMIN

```
ssh sci?
mkdir climate-stripes
git clone https://github.com/agstephens/pystripes
cd pystripes

module load jaspy
python -m venv venv --system-site-packages
source venv/bin/activate

pip install -r requirements.txt
```

## Running an example - for Exmouth

```
# Exmouth is located at: [50.6200, -3.4137]
python make-stripes.py 50.6200 -3.4137
```
 
