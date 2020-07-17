# Corelogic API Python client

## Overview

This is a Python client for the [CoreLogic API](https://developer.corelogic.asia/apis/docs/overview-au).  

I haven't seen any clients for Python, so this is a start. 



## Usage

Install requirements
`pip3 install -r requirements.txt`

Basic usage is can be accessed through Client.py where default parameters are given to for subquries.  
For detailed usage individual end points can be called directly.

[] create an account on [coreLogic developer](https://developer.corelogic.asia/user)  
[] add an config.py file to app/  
[] copy and paste the below into config.py replacing the values
```
account_info = {
    'cid': '<your Client_id>',
    'secret': '<your secret_code>'
}
```


## Tasks

Pull requests and collaboration is greatly welcomed!

- starting with interesting endpoints