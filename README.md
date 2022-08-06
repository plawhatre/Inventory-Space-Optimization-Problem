# TransportationProblem

Consider the following items in the inventory

| name| profit | space |
| --  | ------ | ----- |
| ac  |   23   |  0.1  |
| tv  |   45   |  0.2  |
| tv2 |   23   |  0.1  |
|phone|   11   |  0.3  |
| fan |   11   |  0.5  |

The goal is to select items from this inventory and load it into a transport.
This puts a space constraint on selection. However, the ultimate objective is to maximize the profit.

In this repository, Greedy and Genetic Algorithm are employed to solve this optimization problem. 

## Greedy Algorithm's Output

``` python
OPTIMAL SOL

DataObj(name='tv', profit=45, space=0.2)
DataObj(name='tv2', profit=23, space=0.1)
DataObj(name='ac', profit=23, space=0.1)
DataObj(name='fan', profit=11, space=0.5)
```
It has `Cummulative Profit = 102, Cummlative Space = 0.9`

## Genetic Algorithm's Output 

It generates either of the two solutions

a) `Cummulative Profit = 102, Cummlative Space = 0.7`

``` python
OPTIMAL SOL

DataObj(name='ac', profit=23, space=0.1)
DataObj(name='tv', profit=45, space=0.2)
DataObj(name='tv2', profit=23, space=0.1)
DataObj(name='phone', profit=11, space=0.3)
```

b) `Cummulative Profit = 102, Cummlative Space = 0.9`

``` python
OPTIMAL SOL

DataObj(name='tv', profit=45, space=0.2)
DataObj(name='tv2', profit=23, space=0.1)
DataObj(name='ac', profit=23, space=0.1)
DataObj(name='fan', profit=11, space=0.5)
```