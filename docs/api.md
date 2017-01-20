# API Documentation
ofxclient-python provides a rich API for interacting with OFX servers which can be added to your Python application.
There are two main public-facing classes to work with: `OFXClient` and `OFXParser`.

## OFXClient

```python
from ofxclient.ofxclient import OFXClient
```

### \_\_init\_\_
Constructor

#### Required arguments

| Argument  | Description |
| ------------- | ------------- |
| fi  | `string` indicating a financial institution.  |
| userid  | `string` indicating the user's id.  |
| userpass  | `string` indicating the user's password.  |
| acctid  | `string` indicating the user's account number.  |


### get_transactions 
Returns a list of credit card transactions.

#### Required arguments

| Argument  | Description |
| ------------- | ------------- |
| start_date  | `datetime` object indicating when to begin listing transactions.  |

#### Optional arguments (passed in as `**kwargs`)

- `acctid`: Account/credit card number


## OFXParser
