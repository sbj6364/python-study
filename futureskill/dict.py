planet_kr = ['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
planet_en = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

name = input()
planet = {kr:en for kr, en in zip(planet_kr, planet_en)}
planet[name]
