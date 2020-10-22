# from property import suggest

class UnitTest:
    """Base class for CRAW unit tests."""

    def setup(self):
        """Setup runs before all test cases."""
        sandbox_areas = {}
        property_info = {}
        property_ids = {}
        states = ['ACT', 'NSW', 'VIC', 'QLD', 'NT', 'SA', 'WA']
        suburbs = ['Kambah', 'Monash', 'Oxley', 'Blacktown', 'Quakers Hill', 
                    'Seven Hills', 'Durack', 'Humpty Doo', 'Zuccoli', 'Broadbeach', 
                    'Southport', 'Surfers Paradise', 'Adelaide', 'Glenside', 'North Adelaide', 
                    'Devonport', 'La Trobe', 'Ulverstone', 'Beaconsfield', 'Officer', 
                    'Pakenham', 'Baldivis', 'Cooloongup', 'Rockingham']
        

