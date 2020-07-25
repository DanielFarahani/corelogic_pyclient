from authentication import Authentication
import requests
from requests.exceptions import HTTPError


# under censusServices/ in future
class Census(Authentication):

    def __init__(self):
        super().__init__(False)
        self.base += "/statistics"


    #TODO just push this to census as kwargs
    def summary(self, location_id=12606, location_type_id=8):
        r'''
        returns:
        {
            "censusSummaryDescription": "string",
            "councilAreaName": "string",
            "countryName": "string",
            "errors": [ { "msg": "string" } ],
            "fiveYearPopulationChange": "string",
            "localityName": "string",
            "locationType": "string",
            "postcodeName": "string",
            "stateName": "string",
            "territorialAuthorityName": "string"
        }
        '''
        
        params = {
            'locationId': location_id,
            'locationTypeid': location_type_id
        }

        try:
            res = requests.get(self.url + "/census/summary", params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            print(err) 
        
        return res


# size, parks (#, %), age group, household, repayment (range/m), occupation type, median salary
    def census(
        self, 
        from_date="", 
        to_date="", 
        location_id=12606, 
        location_id_type=8, 
        metric_type_group_id=120, 
        metric_type_id=0
        ):
        r'''
        {
            "censusResponseList": [
                {
                "councilAreaName": "string",
                "countryName": "string",
                "isSumStatistic": true,
                "localityName": "string",
                "locationType": "string",
                "metricDisplayType": "string",
                "metricType": "string",
                "metricTypeDescription": "string",
                "metricTypeGroup": "string",
                "metricTypeGroupDescription": "string",
                "metricTypeGroupId": 0,
                "metricTypeId": 0,
                "metricTypeOrderId": 0,
                "metricTypeShort": "string",
                "postcodeName": "string",
                "propertyType": "string",
                "seriesDataList": [ { "dateTime": "2020-07-25T11:07:20.896Z", "value": 0 } ],
                "stateName": "string",
                "territorialAuthorityName": "string"
                }
            ],
            "errors": [ { "msg": "string" } ]
        }
        '''

        payload = {
            'censusRequestList': [
                {
                    "fromDate": from_date,
                    "locationId": location_id,
                    "locationTypeId": location_id_type,
                    "metricTypeGroupId": metric_type_group_id,
                    "metricTypeId": metric_type_id,
                    "toDate": to_date
                }
            ]
        }

        try:
            res = requests.post(self.url + "/census", data=payload, headers=self.headers).json().__dict__()
            
        except HTTPError as err:
            print(err)

if __name__ == "__main__":
    c = Census()
    print(c.summary())