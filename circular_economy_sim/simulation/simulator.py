from circular_economy_sim.models.sector import Sector

class Simulator:
    def __init__(self, sectors, start_year=2024, end_year=2030):
        self.sectors = sectors
        self.start_year = start_year
        self.end_year = end_year
        self.results = {}

    def run(self):
        for year in range(self.start_year, self.end_year + 1):
            self.results[year] = {}
            for sector in self.sectors:
                waste = sector.project_waste(year)
                recycling = waste * sector.project_recycling(year)
                landfill = waste - recycling
                self.results[year][sector.name] = {
                    'waste': waste,
                    'recycling': recycling,
                    'landfill': landfill
                }
        return self.results 