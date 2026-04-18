
INDIVIDUAL REFLECTIONS


#######################################################################

John Esteve Butad:

Based on the results, the **sequential sorting algorithm** performed well for small and medium datasets.
For 1,000 and 100,000 elements, the sequential method sorted the data correctly and in a reasonable amount of time.
This is because sequential algorithms process the data step by step without additional overhead from multiple processes.

However, when the dataset reached 1,000,000 elements, the execution time became much longer compared to smaller datasets.
This shows that sequential sorting requires more time as the dataset size increases because all operations are handled in a single sequence.
The algorithm still produced accurate results, but performance decreased due to the larger workload.

Overall, sequential sorting algorithms are reliable and efficient for small to medium datasets.
Sequential algorithms are better for simple tasks and manageable data sizes.
Sequential algorithms remain effective, but performance decreases when handling very large datasets.


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

However, as the dataset size increased, the execution time also increased because the algorithm still had to check each element in order. This shows that sequential searching becomes slower with larger datasets since it does not skip or divide the data, and everything is handled in a single continuous process.

Overall, the sequential searching algorithm is reliable and simple to implement, and it performs well for small to medium datasets. However, its performance decreases as the dataset grows because it must always scan elements one by one, making it less efficient for large-scale data.


#######################################################################
