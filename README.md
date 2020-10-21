# Corelogic API Python client

## Overview

This is a Python client for the [CoreLogic API](https://developer.corelogic.asia/apis/docs/overview-au).  

I haven't seen any clients/ wrappers for Python, so this is a start. 



## Usage

Install requirements  
`pip3 install -r requirements.txt`

Basic usage is can be accessed through Client.py where default parameters are given to for subquries.  
For detailed usage individual end points can be called directly.

[] create an account on [coreLogic developer](https://developer.corelogic.asia/user)  
[] add an config.py file to app/  
[] copy and paste your **Client ID** and **Secret** into config.py replacing the values
```
client_id = '<your Client_id>'
secret = '<your secret_code>'
```


## Tasks

Pull requests and collaboration is greatly welcomed!

End point implementation order:
- Automatic Valuation Model (AVM) to get price of a house
- Property details (photos, past sale values, etc.)
- Helper: suggestion services to get property data
- Helper: search service to get address from property data
