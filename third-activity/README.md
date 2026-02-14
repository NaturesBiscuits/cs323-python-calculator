Group Members:
- Achas, Dan Philip
- Belongilot, Clyde Joshua
- Butad, John Esteve
- Flores, John Vincent


Analysis Questions:
1. Differentiate Task and Data Parallelism. Identify which part of the lab
demonstrates each and justify the workload division.
**Ans**
- Task Parallelism means running different tasks at the same time on the same data. In the lab, this is shown in Part A, where SSS, PhilHealth, Pag-IBIG, and tax are computed in parallel for one employee’s salary. The workload is divided by task because each deduction is independent and can be done at the same time. Data Parallelism means running the same task at the same time on different data. In the lab, this is shown in Part B, where the same payroll computation is applied in parallel to multiple employees. The workload is divided by employee because each employee’s payroll is independent and can be processed separately.

2. Explain how concurrent.futures managed execution, including submit(),
map(), and Future objects. Discuss the purpose of with when creating an
Executor.
**Ans**
- submit() sends a function to be run asynchronously and returns a Future object that holds the result. map() runs the same function over a list of inputs in parallel and returns results in order. A Future represents a task that may not be finished yet, and .result() is used to get its output. The with statement is used to properly start and shut down the executor, making sure all threads/processes finish cleanly.

3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did
true parallelism occur?
**Ans**
- ThreadPoolExecutor does not achieve true CPU parallelism for CPU-bound tasks because of Python’s Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time. Even though multiple threads were created, they mostly took turns using the CPU, so true parallelism did not fully occur for heavy computations.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory
space separation and GIL behavior.
**Ans**
- ProcessPoolExecutor uses separate processes, and each process has its own Python interpreter and memory space. This bypasses the GIL, allowing multiple CPU cores to execute tasks at the same time. Because processes run independently, real parallel execution is achieved, making it better for CPU-bound workloads like payroll computations.

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which
approach scales better and why?
**Ans**
-  Data Parallelism with ProcessPoolExecutor scales better for large numbers of employees because each employee’s payroll can be computed independently across multiple CPU cores. Thread-based task parallelism does not scale well for heavy computation due to the GIL and overhead of managing many small tasks. Process-based parallelism can better utilize multi-core hardware for large workloads.

6. Provide a real-world payroll system example. Indicate where Task Parallelism and
Data Parallelism would be applied, and which executor you would use.
**Ans**
-  In a real payroll system, Task Parallelism can be used when computing different components (tax, benefits, deductions) for a single employee, especially if these involve I/O like API calls to government services (use ThreadPoolExecutor). Data Parallelism can be used when processing payroll for thousands of employees in batch at the end of the month (use ProcessPoolExecutor) to distribute employees across CPU cores for faster total processing.

