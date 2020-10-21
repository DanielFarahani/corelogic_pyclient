from authentication import Authentication
import requests
from requests.exceptions import HTTPError
from datetime import datetime


class Suggest(Authentication):

    def __init__(self):
        super().__init__()

        # website: /property/au/v2/suggest.json
        # website: /property/au/parcel/suggest.json
        # postman: /places/places/suggest

        

    def suggest_places(self, instr, limit, units, bodycorp):
        r'''Description: Gives a list of suggestions based on location (street, suburb, state, etc.) input.
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
        '''
        
        endpoint = '/places/places/suggest'
        url = self.base + endpoint
        params = {
            'q': instr,
            'limit': limit
        }

        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            return err
        
        return res
