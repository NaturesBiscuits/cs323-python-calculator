
INDIVIDUAL REFLECTIONS


#######################################################################

John Esteve Butad:

In this activity, I learned that sequential and parallel execution have clear differences. Sequential algorithms are easier to understand since they run step by step, while parallel algorithms split the work and run tasks at the same time, which makes them more complex to handle.

When I tested different dataset sizes, I noticed that sequential execution worked better for small data because it has less overhead. Parallel execution only became faster when the dataset was large enough to benefit from dividing the workload.

One challenge I faced was making sure the parallel version still produced correct results. Handling things like getting the correct index in searching and merging sorted data in parallel sorting was not easy and required careful thinking. So, parallel algorithms are useful for large datasets, but for smaller tasks, sequential algorithms are still more practical and efficient.


#######################################################################

John Vincent Flores:

    Based on the results sequential algorithms did better for medium datasets.
Parallel algorithms only showed an advantage for datasets.
For 1,000 and 100,000 elements sequential methods were faster for 
both sorting and searching. This is because parallel algorithms have overhead from creating and communicating between processes.
This overhead is too much for datasets.

    However with 1,000,000 elements parallel sorting became much faster than sorting.
This shows that parallel processing is more effective for workloads.
Parallel searching was still slower in all cases.

    Searching does not require computation to benefit from parallel execution.
Overall parallel algorithms are more efficient when the dataset is large enough.
Sequential algorithms are better for tasks or simple tasks.
Parallel algorithms are only better for datasets.
Sequential algorithms are better, for medium datasets.

#######################################################################

Clyde Joshua Belongilot:

Based on the execution of the code, the sequential searching algorithm worked by checking each element one by one until the target value was found or the entire list was scanned. For smaller datasets, the process ran quickly because the loop only needed to go through a limited number of elements, making the execution time very short and efficient.

However, as the dataset size increased, the execution time also increased because the algorithm still had to check each element in order. This shows that sequential searching becomes slower with larger datasets since it does not skip or divide the data, and everything is handled in a single continuous process. The sequential searching algorithm is reliable and simple to implement, and it performs well for small to medium datasets. However, its performance decreases as the dataset grows because it must always scan elements one by one, making it less efficient for large-scale data.


#######################################################################
