import numpy as np
from data_container import DataContainer, DataObj
import logging

logger = logging.getLogger(__name__)

class GreedyAlgorithm:
    """ Class for Greedy Algorithm
    """
    def __init__(self, data_container: DataContainer, limit:float) -> None:
        """ Constructor for Greedy Algorithm
        Args
        ----
        data_container :  data in DataContainer object 
        limit : space constraint
        """
        self.data_container = data_container
        self.limit = limit

    def _sort(self) -> None:
        """ Sort the items in the datacontainer
        """
        profits = self.data_container.profits
        profits = np.argsort(profits)[::-1]
        logger.info("Computed profits for items")

        container = [self.data_container[i] for i in profits]
        self.data_container.container = container
        logger.info("Sorted data container accoring to profits")

    def _cumsum(self) -> None:
        """ Cumulative sum of the spaces
        """
        spaces = self.data_container.spaces
        cumsum = np.cumsum(spaces)
        logger.info("Compted cummulative sum of spaces")

        ind_allowed = cumsum < self.limit
        allowed = []
        for i, ind in enumerate(ind_allowed):
            if not ind:
                break
            allowed.append(self.data_container[i])
        self.data_container.container = allowed
        logger.info("Data Container is constrained")

    def print_optimal_solution(self) -> None:
        """
        Print optimal solutions
        """
        logger.info("Printing optimal solutions")
        
        cummulative_profit, cummulative_space = 0, 0
        for data_obj in self.data_container:
            cummulative_profit= cummulative_profit+data_obj.profit
            cummulative_space= cummulative_space+data_obj.space
            print(data_obj)

        logger.info(f"Cummulative Profit = {cummulative_profit}, Cummlative Space = {cummulative_space}")

    def start(self) -> None:
        """ Start the Greedy Algorithm
        """
        logger.info("Starting the Greedy Algorithm")
        self._sort()
        self._cumsum()
        logger.info('\nAlgorithm has terminated !!')
        print('OPTIMAL SOL\n')
        self.print_optimal_solution()