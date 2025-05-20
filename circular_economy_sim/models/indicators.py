class Indicators:
    def __init__(self, initial_ghg, initial_resource_efficiency, initial_circularity):
        self.initial_ghg = initial_ghg  # tonnes CO2e/year
        self.initial_resource_efficiency = initial_resource_efficiency
        self.initial_circularity = initial_circularity

    def project_ghg(self, year, waste, recycling, landfill):
        # Simple model: GHG emissions proportional to landfill waste
        landfill_factor = 0.5  # tonnes CO2e per tonne of landfill waste
        return landfill * landfill_factor

    def project_resource_efficiency(self, year, gdp, waste):
        # Resource efficiency = GDP / waste
        return gdp / waste if waste > 0 else 0

    def project_circularity(self, year, recycling, waste):
        # Circularity index = recycling / waste
        return recycling / waste if waste > 0 else 0 