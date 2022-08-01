import numpy as np
import pandas as pd
from data_container import DataContainer
import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm
import yaml

if __name__ == '__main__':

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

    # Load data
    df = pd.read_csv(data_file_path)
    data_tuple_list = [tuple(x) for x in df.to_records(index=False)]

    # Create Data Container
    data_container = DataContainer(data_tuple_list)
    
    # Start the Genetic Algorithm
    ga = GeneticAlgorithm(n_chromo, data_container, limit, cross, mutation_prob)
    pp = ga.start_simutation(n_gens, eps, eps_count)

    # Plot fitness over generations
    # plt.plot(pp)
    # plt.show()

