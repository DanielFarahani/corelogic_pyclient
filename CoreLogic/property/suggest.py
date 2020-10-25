import requests
from requests.exceptions import HTTPError
from datetime import datetime

# sys.path.append('../')
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from authentication import Authentication


class Suggest(Authentication):
    def __init__(self, country='au', version='v2', properties=True):
        super().__init__()
        self.version = version
        
        self.base += f'/property/au' if properties else '/places/places'


    def suggest_properties(self, search, parcel=True,
        stype="address, street, locality, postcode", 
        limit=10, 
        units=True, 
        bodycorp=True, 
        returnSuggest='datail'):
        """Description: Gives a list of suggestions based on location (street, suburb, state, etc.) input.
            input: address, street (min 3 char), suburb or state (min 2 char). 
            suggestType: "address, street, locality, postcode, territorialAuthority, councilArea, state, country"
            Limit: number of suggestions returned (default 10)
            includesUnits: unit property type (default True)
            includesBodyCorp: include body corporates (default True)
            returnSuggestion: {only, byType, detail}
            returns: {"suggestions": [{
                "councilAreaId": 0,
                "countryId": 0,
                "isBodyCorporate": true,
                "isUnit": true,
                "localityId": 0,
                "postcodeId": 0,
                "propertyId": 0,
                "stateId": 0,
                "streetId": 0,
                "suggestion": "string",
                "suggestionId": 0,
                "suggestionType": "string",
                "territorialAuthorityId": 0}
                ]
                "systemInfo": {
                    "instanceName": "string",
                    "requestDate": "string"}
            }
        """

        # NOTE state abbreviation doesnt work (Contant corelogic)

        endpoint = '/parcel/suggest.json' if parcel else f'v{self.version}/suggest.json'
        url = self.base + endpoint

        params = {
            'q': search,
            'limit': limit,
            'units': units,
            'bodycorp': bodycorp,
            'returnSuggest': returnSuggest,
        }
        
        if not parcel:
            params['type'] = stype

        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()

        except HTTPError as err:
            return err
        
        return res


    def suggest_places(parameter_list):
        """
            Suggests places like schools based on filter options.
        """
        pass



if __name__ == "__main__":
    import sys
    
