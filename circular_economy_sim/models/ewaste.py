class EWaste:
    def __init__(self, initial_waste, recycling_rate, targets):
        self.initial_waste = initial_waste  # tonnes/year
        self.recycling_rate = recycling_rate
        self.targets = targets

    def project_waste(self, year, growth_rate=0.05):
        # Simple exponential growth model
        years = year - 2024
        return self.initial_waste * ((1 + growth_rate) ** years)

    def project_recycling(self, year):
        # Linear interpolation to target
        if year >= 2025:
            return self.targets.get('recycling', self.recycling_rate)
        else:
            return self.recycling_rate + (self.targets.get('recycling', self.recycling_rate) - self.recycling_rate) * ((year - 2024) / (2025 - 2024))

    def project_landfill(self, year):
        waste = self.project_waste(year)
        recycling = waste * self.project_recycling(year)
        return waste - recycling 