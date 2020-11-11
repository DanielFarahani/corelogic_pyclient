# Corelogic API Python client

## Overview

This is a Python client for the [CoreLogic API](https://developer.corelogic.asia/apis/docs/overview-au).  
Makes interfacing with the API much easier.

I haven't seen any clients/ wrappers for Python, so this is a start. 


## Usage

1. Install requirements  
`pip3 install -r requirements.txt`

2. create an account on [coreLogic developer](https://developer.corelogic.asia/user)  
3. add **Client ID** and **Secret** to enviroment variable
```
#E.g. setup.sh (Then chmod +x setup.sh)
#!/bin/bash
client_id='<Your Client_id>'
secret='<Your secret_code>'
```
```
#or export in the terminal
export client_id='<Your Client_id>'
export secret='<Your secret_code>'
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
