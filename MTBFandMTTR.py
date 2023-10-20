import random

def generate_random_mtbf_mttr():
    # Generera slumpmässiga MTBF och MTTR-värden i sekunder
    mtbf = random.uniform(1000, 10000)  # Exempelvis mellan 1000 och 10000 sekunder
    mttr = random.uniform(10, 300)  # Exempelvis mellan 10 och 300 sekunder

    return mtbf, mttr

# Anropa funktionen för att generera värden
mtbf, mttr = generate_random_mtbf_mttr()

# Skriv ut resultaten
print(f"Slumpmässigt MTBF: {mtbf} sekunder")
print(f"Slumpmässigt MTTR: {mttr} sekunder")
