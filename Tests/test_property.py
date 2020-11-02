import os, sys
import requests
import unittest
import json
from api_env_info import sandbox_env

sys.path.append('../')
from corelogic.property import (suggest, search, valuations, details)


class TestProperty(unittest.TestCase):
    def setup(self):
        """Setup runs before all test cases."""       
        self.suburbs_dict = dict()
        self.raw_proIds_dict = dict()
        self.propertyIds_dict = dict()
        self.valuations = dict()

    # Get suburb ids based on Sandbox data
    def suggestion_nonparcel_test(self):
        sug = suggest.Suggest()
        for states in sandbox_env['Australia']:
            for suburbs in sandbox_env['Australia'][states]:
                suggestions = sug.suggest_properties(suburbs, limit=50)['suggestions']

                if suggestions:
                    for suggestion in suggestions:
                        try:
                            self.suburbs_dict[suburbs].append(suggestion['localityId'])
                        except:
                            self.suburbs_dict[suburbs] = [suggestion['localityId']]
    
    def suggestion_parcel_test(self):
        sug = suggest.Suggest()
        for states in sandbox_env['Australia']:
            for suburbs in sandbox_env['Australia'][states]:
                suggestions = sug.suggest_properties(suburbs, limit=50)['suggestions']

                if suggestions:
                    for suggestion in suggestions:
                        loc = suggestion['suggestion']
                        try:
                            self.raw_proIds_dict[loc].append(suggestion['propertyId'])
                        except:
                            self.raw_proIds_dict[loc] = (suggestion['propertyId'])


    # Get unique propertyIds for the Sandbox data
    def search_test(self):
        s = search.Search()
        for suburbs, codes in self.suburbs_dict.items():
            for code in codes:
                prop_list = s.property_search('locality', code)['_embedded']['propertySummaryList']
                for prop in prop_list:
                    prop = prop['propertySummary']
                    self.propertyIds_dict[prop['id']] = prop['address']['singleLineAddress']


    # Get valuation for peropertyIds
    def avm_test(self):
        v = valuations.Valuations()
        for sug, pid in self.raw_proIds_dict.items():
            valuation = v.consumer(pid)
            self.valuations[pid] = valuation['valution']


if __name__ == "__main__":
    t = TestProperty()
    t.setup()
    # t.suggestion_parcel_test()
    # with open('sandbox_data.json', 'w') as fp:
    #     json.dump(t.raw_proIds_dict, fp)

    # t.search_test()
    # with open('sandbox_addresses.json', 'w') as fp:
    #     json.dump(t.propertyIds_dict, fp)

    ## Property detail test
    # d = details.Details()
    # res = d.property_attributes(1111865)

    # print(len(res))
    # v = valuations.Valuations()
    # res = []
    # for sug, pid in data.items():
    #     res.append(v.consumer(pid))
    # t.avm_test()
    # print(self.valuations)
