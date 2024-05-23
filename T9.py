def get_species_list(coordinate, radius):
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={coordinate['latitude']},{coordinate['longitude']},{radius}"
    response = requests.get(url)
    data = response.json()
    if "SpeciesSightingSummariesContainer" in data:
        return data["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
    else:
        return []
