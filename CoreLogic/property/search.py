import requests
from datetime import datetime
from ..authentication import Authentication



class Search(Authentication):

    def __init__(self, country='au', env=""):
        # Docs: https://developer.corelogic.asia/apis/docs/search-au
        super().__init__(config=env)
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
            Description: gives list of potential poperties that match the id
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

    def address_search(self, address, **kwargs):
        """
            Description: give PID for address
            string: address string [numer][street][street type][suburb][state][postcode]
            returns: {"propertyAddress": [
                    {"isActiveProperty": true,
                     "propertyId": 1111865,
                     "singleLineAddress": "6 Alabaster Street Monash ACT 2904"
                    }]} 
        """
        
        endpoint = f'/address'
        url = self.base + endpoint

        params = {'singleLineAddress': address,} if not kwargs else kwargs

        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            return err
        return res


    def database_search(self, address, clientName="", matchProfileId=""):
        """
            Description: Searches the database to see if the property exists
            string: address string [numer][street][street type][suburb][state][postcode]
            ClientName: name of client requesting
            MatchProfileID: matching type
            returns: {"matchDetails": {
                    "matchRule": "064",
                    "matchType": "M",
                    "updateDetail": "00009959",
                    "updateIndicator": "U"
                    }
                }
        """

        self.base += '/matcher'
        params = {'singleLineAddress': address}
        return self.address_search(address, params)



if __name__ == "__main__":
    s = Search()

