import haversine as hs   
from haversine import Unit

def get_distance(locations, home, destination):
    home_loc = (locations.loc[home]['lat'], locations.loc[home]['lng'])
    destination_loc = (locations.loc[destination]['lat'], locations.loc[destination]['lng'])
    try:
        return hs.haversine(home_loc, destination_loc, unit=Unit.KILOMETERS)
    except ValueError:
        print(f'Got unexpected values {home_loc} and {destination_loc} for {home} and {destination}')
        raise

def append_distances_from_wh(locations, wh_city_state):
    distances = {}
    for destination in locations.index:
        distance = get_distance(locations, wh_city_state, destination)
        distances[destination]=distance
        locations[f'{wh_city_state}_dist'] = locations.index.map(distances)