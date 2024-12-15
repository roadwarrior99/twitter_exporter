# twitter_exporter


## SETUP
Install python 3.12

Download or git clone this library to folder of your choice

Open a command line window to your folder of choice for this program to live.
## Create your python virtual environment
python3 -m venv .venv

run .venv/bin/activate

your console should look like
(.venv) whatever

next we will install the required dependencies

pip install -r requirements.txt

## twitter exporters is now ready for use.

# usage
python3 export.py --json-file-in twitter.json --excel-file-out twiter.xlsx


## FYI
It is required to activate your python virtual environment
before you call export.py or else you will get a dependency error.
