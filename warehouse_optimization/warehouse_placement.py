# This work relies on a pickle created by warehouse_placement.ipynb
import time
from multiprocessing import Pool

import pandas as pd

import common


pickle_path = "../data/city_weight_agg.pkl"



def print_optimal_weight_distance(new_wh):
    df = pd.read_pickle(pickle_path)
    common.append_distances_from_wh(df, new_wh)

    # We'll establish the warehouse that's closest to the destination
    df['optimal_dist'] = df[['Dallas_TX_dist', f'{new_wh}_dist']].min(axis=1)
    df['from_dallas'] = (df['Dallas_TX_dist'] < df[f'{new_wh}_dist'])

    # This gives a total of the number of cities served by each warehouse
    from_dallas = df.from_dallas.value_counts()[True]
    from_away = df.from_dallas.value_counts()[False]


    # We'll get the optimal kg*km sum as well
    df['weight_distance_shipped'] = df['optimal_dist'] * df['net_weight']
    optimal_weight_distance = df['weight_distance_shipped'].sum()
    print(f'{new_wh},{optimal_weight_distance},{from_dallas},{from_away}')


def pool_handler(possible_wh_locations):
    p = Pool(4)
    p.map(print_optimal_weight_distance, possible_wh_locations)


if __name__ == '__main__':
    temp = pd.read_pickle(pickle_path)
    possible_wh_locations = temp.index.values

    start_time = time.time()
    # To run the full set get rid of the slicing here
    pool_handler(possible_wh_locations[0:5])
    print("--- %s seconds ---" % (time.time() - start_time))


