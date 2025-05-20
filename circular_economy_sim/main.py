from data.baseline_data import (
    PLASTIC_WASTE_DHAKA_TPD, PLASTIC_RECYCLED_PCT, NATIONAL_PLASTIC_RECYCLING_TARGET_2025,
    TEXTILE_WASTE_GENERATION_TPY, TEXTILE_RECYCLING_RATE, TEXTILE_RECYCLING_TARGET_2025,
    TOTAL_WASTE_GENERATION_TPY, WASTE_RECYCLING_RATE, WASTE_RECYCLING_TARGET_2025
)
from models.sector import Sector
from models.agriculture import Agriculture
from models.construction import Construction
from models.ewaste import EWaste
from models.economy import CircularEconomy
from models.policy import PolicyLever
from models.indicators import Indicators
from simulation.simulator import Simulator

# Convert daily plastic waste to yearly
plastic_waste_dhaka_year = PLASTIC_WASTE_DHAKA_TPD * 365

# Initialize sector models
plastic_sector = Sector(
    name="Plastics",
    waste_generation=plastic_waste_dhaka_year,
    recycling_rate=PLASTIC_RECYCLED_PCT,
    targets={'recycling': NATIONAL_PLASTIC_RECYCLING_TARGET_2025}
)

textile_sector = Sector(
    name="Textiles",
    waste_generation=TEXTILE_WASTE_GENERATION_TPY,
    recycling_rate=TEXTILE_RECYCLING_RATE,
    targets={'recycling': TEXTILE_RECYCLING_TARGET_2025}
)

waste_sector = Sector(
    name="Waste Management",
    waste_generation=TOTAL_WASTE_GENERATION_TPY,
    recycling_rate=WASTE_RECYCLING_RATE,
    targets={'recycling': WASTE_RECYCLING_TARGET_2025}
)

# Initialize new sector models
agriculture_sector = Agriculture(
    initial_waste=1_000_000,  # tonnes/year
    recycling_rate=0.10,
    targets={'recycling': 0.20}
)

construction_sector = Construction(
    initial_waste=2_000_000,  # tonnes/year
    recycling_rate=0.15,
    targets={'recycling': 0.30}
)

ewaste_sector = EWaste(
    initial_waste=100_000,  # tonnes/year
    recycling_rate=0.05,
    targets={'recycling': 0.15}
)

# Initialize economy model
economy = CircularEconomy(
    initial_gdp=300_000_000_000,  # USD
    gdp_growth_rate=0.06,
    initial_resource_efficiency=0.3
)

# Initialize policy levers
plastic_tax = PolicyLever(
    name="Plastic Tax",
    impact_factor=0.1,
    start_year=2025,
    end_year=2030
)

recycling_incentive = PolicyLever(
    name="Recycling Incentive",
    impact_factor=0.15,
    start_year=2024,
    end_year=2030
)

# Initialize indicators
indicators = Indicators(
    initial_ghg=10_000_000,  # tonnes CO2e/year
    initial_resource_efficiency=0.3,
    initial_circularity=0.2
)

# Run simulation
sim = Simulator([plastic_sector, textile_sector, waste_sector, agriculture_sector, construction_sector, ewaste_sector])
results = sim.run()

# Print results
for year, data in results.items():
    print(f"Year: {year}")
    for sector, vals in data.items():
        print(f"  {sector}: Waste={vals['waste']:.0f}t, Recycling={vals['recycling']:.0f}t, Landfill={vals['landfill']:.0f}t") 