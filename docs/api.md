# API Documentation
ofxclient-python provides a rich API for interacting with OFX servers which can be added to your Python application.
There are two main public-facing classes to work with: `OFXClient` and `OFXParser`.

## :dollar: OFXClient

```python
from ofxclient.ofxclient import OFXClient
```

### :star: \_\_init\_\_
Constructor

#### Required arguments

| Argument  | Description |
| ------------- | ------------- |
| fi  | `string` indicating a financial institution.  |
| userid  | `string` indicating the user's id.  |
| userpass  | `string` indicating the user's password.  |
| acctid  | `string` indicating the user's account number.  |


### :star: get_transactions 
Returns a list of credit card transactions.

#### Required arguments

| Argument  | Description |
| ------------- | ------------- |
| start_date  | `datetime` object indicating when to begin listing transactions.  |

#### Optional arguments (passed in as `**kwargs`)

- `acctid`: Account/credit card number


## :dollar: OFXParser

```python
from ofxclient.ofxparser import OFXParser
```

### :star: as_json
Format `data` as JSON-encoded string.

#### Required arguments

| Argument  | Description |
| ------------- | ------------- |
| data  | `str` of OFX-formatted data to turn to JSON.  |

#### Optional arguments

- `pretty`: Format the keys in a more readable way (default False).
- `**filters`: Dictionary of functions, mapped to keys to filter the data.
