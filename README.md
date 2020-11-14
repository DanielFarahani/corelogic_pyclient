# Corelogic API Python client

## Overview

This is a Python client for the [CoreLogic API](https://developer.corelogic.asia/apis/docs/overview-au).  
Makes interfacing with the API much easier.

I haven't seen any clients/ wrappers for Python, so this is a start. 

## install
```bash
pip3 install corelogic-pyclient
OR
pip install corelogic-pyclient
```

## Usage 
1. create an account on [developer.corelogic](https://developer.corelogic.asia/user) for a API credentials
2. add **Client ID** and **Secret** to enviroment variable  
> bash script to run everytime
```bash
#E.g. create setup.sh (Then chmod +x setup.sh)
#!/bin/bash
client_id='<Your Client_id>'
secret='<Your secret_code>'
```
> OR manual process
```bash
#or export in the terminal
export client_id='<Your Client_id>'
export secret='<Your secret_code>'
```
3. Import
```python
>>> import corelogic.property as prop
>>> details = prop.Details()
>>> details.property_attributes(<property_id>)
{'beds': 2, 'baths': 1, ...}

>>> suggestions = prop.Suggest()
>>> suggestions.suggest_properties('1 ahern place monash')
```



### Endpoints

The structure of the package is similar to the Postman [collection provided](https://documenter.getpostman.com/view/7051651/S1EJWfxt) by CoreLogic.  
You can import class/folder of the API separately and use the endpoint through the methods.

* Suggestion
* Search
* Property Detail
* Automatic Valuation model (AVM)



## Tasks
Pull requests and collaboration is greatly welcomed!

- build out the endpoints of interest
- Refactor to better form factor
- Complete Health check
- Complete Tests

## Goals
- Given the API is $ per request scheme it would be good to cache
- reduce the API endpoints from the website to minimal set as there is alot of overlap in response data
- Better error handling
- Look for API version updates
- Better messaging for the response payload
