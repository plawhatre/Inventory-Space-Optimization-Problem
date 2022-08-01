"""
Data object and Container classes
"""

from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass(order=True)
class DataObj:
    """ DataObj creates an object for each record in data
    Args
    ----
    name: Name of the product
    profit: Profit in shipping the product
    space: Space occupied by the product on the transport
    """
    sort_index: int = field(init=False, repr=False)
    name: str
    profit: int
    space: float
    
    def __post_init__(self):
        self.sort_index = self.profit

class DataContainer:
    """ Data Container class holding objects of DataObj class
    """
    def __init__(self, data_tuple_list: List[Tuple[str, int, float]]) -> None:
        self.container = []
        for data_tuple in data_tuple_list:
            self.container.append(DataObj(*data_tuple))

    def __len__(self) -> int:
        """
        Returns
        ------
        Number of products in the inventory
        """
        return len(self.container) 

    def __getitem__(self, n: int) -> DataObj:
        """ Gets product according to the index
        Returns
        -------
        Product in the inventory according to the index
        """
        return self.container.__getitem__(n)

    def get_val_indices(self, indices: List[int]) -> List[DataObj]:
        """ Gets product according to the indices
        Returns
        -------
        Products in the inventory according to the indices
        """
        return [self[index] for index in indices]

    def get_val_bindices(self, indices: List[int]) -> List[DataObj]:
        """ Gets product according to the indices in binary form
        Returns
        -------
        Products in the inventory according to the indices in binary form
        """
        indices = [index for index, val in enumerate(indices) if val==1]
        return self.get_val_indices(indices)
    
    @property
    def names(self) -> List[str]:
        """
        Returns
        -------
        Names of the products in the inventory
        """
        return [data_obj.name for data_obj in self.container]

    @property
    def profits(self) -> List[int]:
        """
        Returns
        -------
        Profits on the products in the inventory
        """
        return [data_obj.profit for data_obj in self.container]

    @property
    def spaces(self) -> List[float]:
        """
        Returns
        -------
        Space occupied by each product in the inventory
        """
        return [data_obj.space for data_obj in self.container]
