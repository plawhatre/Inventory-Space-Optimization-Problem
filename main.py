#!/usr/bin/env python3 
import numpy as np
import pandas as pd
from data_container import DataContainer
from genetic_algorithm import GeneticAlgorithm
from greedy_algorithm import GreedyAlgorithm
import yaml
import logging
import argparse

from greedy_algorithm import GreedyAlgorithm

if __name__ == '__main__':

    # set up logger
    handlers = [logging.FileHandler(filename='log.log'), logging.StreamHandler()]
    logging.basicConfig(
                        handlers = handlers,
                        format='%(filename)s %(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s', 
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)
                        
    logger = logging.getLogger(__name__)

    # Load params
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)

    # Load constants
    data_file_path = params['data_file_path']
    n_chromo = params['n_chromo']
    limit = params['limit']
    cross = params['cross']
    mutation_prob = params['mutation_prob']
    n_gens = params['n_gens']
    eps = params['eps']
    eps_count = params['eps_count']

    if not isinstance(eps_count, int):
        eps_count = n_gens

    logger.info("Finished loading constants in main")

    # Load data
    df = pd.read_csv(data_file_path)
    data_tuple_list = [tuple(x) for x in df.to_records(index=False)]
    
    logger.info("Finished loading data in main")

    # Create Data Container
    data_container = DataContainer(data_tuple_list)

    logger.info("Created data container")

    
    parser = argparse.ArgumentParser()
    parser.add_argument('--setdefault', help="Run Genetic algorithm")
    args = parser.parse_args()
    if args.setdefault:
        # Start the Genetic Algorithm
        ga = GeneticAlgorithm(n_chromo, data_container, limit, cross, mutation_prob)
        _ = ga.start_simutation(n_gens, eps, eps_count)

    else:
        # Start the Greedy Algorithm
        ga = GreedyAlgorithm(data_container, limit)
        ga.start()

    logger.info("Finished runing algorithm")

