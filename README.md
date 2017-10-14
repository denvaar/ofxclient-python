# ofxclient-python
Open Financial Data Exchange (OFX) client API and command-line interface

# Description
Open Financial Exchange (OFX) is the open standard for interacting with financial data from financial institutions. It's developed and maintained by a consortium of financial application developers, aggregation services, and financial services providers. More information can be found at [ofx.org](http://www.ofx.org/index.html).

This is a Python API, and also a command-line interface for interacting with OFX (version 2.0+) servers. Check out the docs for more information:
- [API](docs/api.md)
- [Command-line interface tool](docs/ofxclient-cli.md)

# Requisites

Python 3 with version >= 3.4 

# Installation with pip

`pip install ofxclient-python==0.0.5`

# Installation with pyinstaller

`pip install pyinstaller`

Then from root repo go into ofxclient directory to create executable  
`cd ofxclient`  
`pyinstaller ofxclient-cli.py` 

This will create a dist directory that will contains everything needed to run the program.  
To use the program run it from this directory  
`cd dist/ofxclient-cli`
`ofxclient-cli`

## Development
Just grab a copy the repository and pip install the requirements found in `requirements.txt`.

# Usage

*TODO examples*

# Contributing

Please feel free.
