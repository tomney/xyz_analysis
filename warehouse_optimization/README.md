# Instruction
A dummy version of the entire workflow can be run exclusively within the notebook. To capitalize on parallelization though and analyze all potential sites for a new warehouse follow the following steps:
 - run the steps in the notebook up until the pickle file is created
 - run the code `python warehouse_placement.py > ../data/weight_distances_log_dummy.csv` to parallelize execution this may take a few hours based on the number of cores available
 - run the last two cells of `warehouse_placement.ipynb`