# cs323-python-calculator
## Group Members
Clyde Belongilot
Dan Philip Achas
John Esteve Butad
John Vincent Flores

## Second Laboratory

<img width="661" height="397" alt="image" src="https://github.com/user-attachments/assets/646e1330-3ff5-4e07-95fd-4eec6f3a5439" />


**1. Which approach demonstrates true parallelism in Python? Explain.**
Multiprocessing, since it runs on a separate CPU core allowing each to execute simultaneously.

**2. Compare execution times between multithreading and multiprocessing.**
In our run, Multithreading was slightly faster with 1.4746 seconds than Multiprocessing that has 1.5896 seconds. This is due to multithreading having lower overhead in creating threads compared to multiprocessing that spawns processes.

**3. Can Python handle true parallelism using threads? Why or why not? 

**4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?** 
No, due to Global Interpreter Lock (GIL), it simply cannot achieve true parallelism, GIL allows only one thread to execute Python bytecode at a time.

**5. Which method is better for CPU-bound tasks and which for I/O-bound tasks? **
Multiprocessing is better for CPU-bound task, while multithreading is betting for I/O bound tasks due to lower overhead and efficient waiting on I/O

**6. How did your group apply creative coding or algorithmic solutions in this lab?** 
We labeled outputs for clear analysis, and measured execution time to compare concurrency behavior and performance, that way it is easy for us to analyze the data and write observations.

We use live code to test our changes and push to one account, while one of our members observes to write for the table, while we all observe.
