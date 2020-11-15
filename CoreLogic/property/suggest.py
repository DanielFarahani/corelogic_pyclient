import requests
from datetime import datetime
from ..authentication import Authentication


class Suggest(Authentication):
    def __init__(self, country='au', version='2', properties=True, env=""):
        super().__init__(config=env)
        self.version = version
        self.base += f'/property/au' if properties else '/places/places'


    def suggest_properties(self, search, parcel=True,
        stype="address,street,locality,postcode", 
        limit=10, 
        units='TRUE', 
        bodycorp='TRUE', 
        returnSuggest='datail'):
        """
            Description: Gives a list of suggestions based on location (street, suburb, state, etc.) input.
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

        endpoint = '/parcel/suggest.json' if parcel else f'/v{self.version}/suggest.json'
        url = self.base + endpoint

        # params = {
        #     'q': search,
        #     'limit': limit,
        #     'includeUnits': units,
        #     'includeBodyCorporates': bodycorp,
        #     'returnSuggestion': returnSuggest,
        #     }
            
        # if not parcel:
        #     params['suggestionTypes'] = stype

        # TODO detect non-default params 
        params = {'q':search}


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
