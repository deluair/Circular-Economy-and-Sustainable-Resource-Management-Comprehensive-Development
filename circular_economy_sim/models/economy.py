class CircularEconomy:
    def __init__(self, initial_gdp, gdp_growth_rate, initial_resource_efficiency):
        self.initial_gdp = initial_gdp
        self.gdp_growth_rate = gdp_growth_rate
        self.initial_resource_efficiency = initial_resource_efficiency

    def project_gdp(self, year):
        # Simple exponential growth model
        years = year - 2024
        return self.initial_gdp * ((1 + self.gdp_growth_rate) ** years)

    def project_resource_efficiency(self, year, target_efficiency=0.5):
        # Linear interpolation to target efficiency
        if year >= 2030:
            return target_efficiency
        else:
            return self.initial_resource_efficiency + (target_efficiency - self.initial_resource_efficiency) * ((year - 2024) / (2030 - 2024)) 