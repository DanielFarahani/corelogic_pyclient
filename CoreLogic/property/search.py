from authentication import Authentication
import requests
from requests.exceptions import HTTPError
from datetime import datetime

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from authentication import Authentication



class Search(Authentication):

    def __init__(self, country='au'):
        # variations: search, property, places, Location
        super().__init__()
        self.base += f'/search/{country}'


    def property_search(self, stype, id, 
        country='au', 
        sort="address,asc", 
        size=20,
        page=0, 
        baths="0-", 
        beds="0-", 
        carSpace="0-", 
        landArea="0-", 
        pTypes=""):
        """
        Description: gives results
        type: type of id given for the search {street, place, locality, councilArea, Postcode}
        id: the ID of the search from "CoreLogic Suggest Service"
        Optionals: sort, size, page, baths, beds, carspace, landarea, pTypes
        'UNIT', 'FLATS', 'COMMERCIAL', 'HOUSE', 'LAND', 'BUSINESS', 'OTHER', 'COMMUNITY', 
        'FARM', 'STORAGE_UNIT'
        returns: Schema 
        """
        
        endpoint = f'/property/{stype}/{id}'
        url = self.base + endpoint

        params = {
            'sort': sort, 'size': size,
            'page': page, 'baths': baths,
            'beds': beds, 'carSpace': carSpace,
            'landArea': landArea, 'pTypes': pTypes,
        }

        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()

        except HTTPError as err:
            return err
        
        return res


    def property_last_sale_search():
        endpoint = '/lastSale'
        pass


if __name__ == "__main__":
    s = Search()

