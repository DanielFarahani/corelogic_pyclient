# Corelogic API Python client

## Overview

This is a Python client for the [CoreLogic API](https://developer.corelogic.asia/apis/docs/overview-au).  

I haven't seen any clients/ wrappers for Python, so this is a start. 


## Usage

Install requirements  
`pip3 install -r requirements.txt`

[] create an account on [coreLogic developer](https://developer.corelogic.asia/user)  
[] add an config.py file to app/  
[] copy and paste your **Client ID** and **Secret** into config.py replacing the values
```
client_id = '<your Client_id>'
secret = '<your secret_code>'
```

The structure of the package is similar to the Postman [collection provided](https://documenter.getpostman.com/view/7051651/S1EJWfxt) by CoreLogic.


## Tasks

Pull requests and collaboration is greatly welcomed!

End point implementation order:
- Automatic Valuation Model (AVM) to get price of a house
- Property details (photos, past sale values, etc.)
- Helper: suggestion services to get property data
- Helper: search service to get address from property data
