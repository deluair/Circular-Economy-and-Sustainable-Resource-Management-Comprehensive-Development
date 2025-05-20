class PolicyLever:
    def __init__(self, name, impact_factor, start_year, end_year):
        self.name = name
        self.impact_factor = impact_factor  # e.g., 0.1 for 10% improvement
        self.start_year = start_year
        self.end_year = end_year

    def is_active(self, year):
        return self.start_year <= year <= self.end_year

    def apply_impact(self, base_value, year):
        if self.is_active(year):
            return base_value * (1 + self.impact_factor)
        return base_value 