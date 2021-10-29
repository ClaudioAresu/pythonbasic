from dataclasses import dataclass, field
import abc


@dataclass
class Biomes:

    majorBiome: str
    minorBiome: str="nothing"

biome1 = Biomes("Tropical and Subtropical Moist Forest")

print(biome1)