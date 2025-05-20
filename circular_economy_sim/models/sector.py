class Sector:
    def __init__(self, name, waste_generation, recycling_rate, targets):
        self.name = name
        self.waste_generation = waste_generation  # tonnes/year
        self.recycling_rate = recycling_rate
        self.targets = targets

    def project_waste(self, year, growth_rate=0.03):
        # Simple projection: exponential growth
        years = year - 2024
        return self.waste_generation * ((1 + growth_rate) ** years)

    def project_recycling(self, year):
        # Linear interpolation to target
        if year >= 2025:
            return self.targets.get('recycling', self.recycling_rate)
        else:
            return self.recycling_rate + (self.targets.get('recycling', self.recycling_rate) - self.recycling_rate) * ((year - 2024) / (2025 - 2024)) 