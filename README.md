# Loading Balancing Algorithms Comparison

This project implements and compares two different algorithms for Loading Balancing problem. The problem can be found in the book "Algorithm Design" by Jon Kleinberg and Éva Tardos. The project includes an optimal algorithm using dynamic programming and an approximation algorithm using the greedy technique.

## Project Context

This project was part of an assignment for the Analysis of Algorithms course in the Master's program in Computer Science at the Federal University of Uberlândia (UFU). The presentation file can be found in 'load-balancing.pdf' (presentation in Portuguese).

## Algorithms Implemented

1. **Optimal Algorithm with Dynamic Programming**
   - Calculates the best way to allocate n tasks in m machines in order to minimize the makespan. It calculates all possibilities to find the best one.

2. **Greedy Approximation Algorithm**
   - Uses greedy technique to find an approximation best solution in less time than the optimal algorithm.

## Files

- **loadBalancingDynamicProgramming.py**: Implementation of the optimal algorithm.
- **loadBalancingGreedy.py**: Implementation of the greedy approximation algorithm.
- **compareAlgorithms.py**: Script to compare the execution time of all algorithms across a range of input sizes.

## Running the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/tiagohugovitor/load-balancing-eva-tardos.git
   cd load-balancing-eva-tardos
   ```

2. Run the comparison script:
    ```bash
    python compareAlgorithms.py
    ```

3. Results:
    - Execution time graphs saved in the results directory as figure-{numberOfMachines}-machines-{numberOfJobs}-jobs.png
    - Dataframe with execution times saved in the results directory as dataframe-{numberOfMachines}-machines-{numberOfJobs}-jobs.xlsx.

## Algorithms Analysis

### Time Complexity
 - **Optimal Algorithm with Dynamic Programming**: O(n ⋅ m² ⋅ S^{m}), where n is number of jobs, m is number machines and S is the sum of all tasks times.
 - **Greedy Approximation Algorithm**: O(n logn + n ⋅ (m - 1)), where n is number of jobs and m is number machines.

### Space Complexity
 - **Optimal Algorithm with Dynamic Programming**: O(2S^{m}) = O(S^{m}), where m is number machines and S is the sum of all tasks times.

### Approximation Ratio
The approximation ratio of an algorithm is a measure of how close the solution provided by the algorithm is to the optimal solution. For the approximate algorithm used in this project, the approximation ratio is T &leq; 1.5T^{ * }, where T is the response from the approximation algorithm and T^{*} is the optimal response. In the tests run, the approximate algorithm's error rate increases with the number of machines, though it maintains a higher success rate with a larger number of tasks.

### Conclusion
The optimal algorithm exhibits an exponential time complexity relative to m, specifically O(n⋅m⋅S^{m}). When n is considered constant, this reduces to O(m⋅c^{m}). Conversely, the algorithm has a polynomial time complexity relative to n, represented as O(n⋅m⋅S^{m}), which simplifies to O(n⋅n^c) when m is constant. Additionally, the optimal algorithm requires extra space of O(S^{m}) due to the use of dynamic programming.

The approximate algorithm, on the other hand, has a linear execution time relative to m, described by O(n⋅logn + n⋅m). When n is constant, this becomes O(c⋅logc + cm) = O(m). The execution time is n⋅logn relative to n, simplifying to O(n⋅logn + nc) = O(n⋅logn) when m is constant. However, the approximate algorithm's error rate increases with the number of machines, though it maintains a higher success rate with a larger number of tasks.

## Dependencies
    - Python 3.x
    - matplotlib
    - pandas