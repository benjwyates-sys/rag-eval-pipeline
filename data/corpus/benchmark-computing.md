# Benchmark (computing)

In computing, a benchmark is the act of running a computer program, a set of programs, or other operations, in order to assess the relative performance of an object, normally by running a number of standard tests and trials against it.
The term benchmark is also commonly utilized for the purposes of elaborately designed benchmarking programs themselves.
Benchmarking is usually associated with assessing performance characteristics of computer hardware, for example, the floating point operation performance of a CPU, but there are circumstances when the technique is also applicable to software. Software benchmarks are, for example, run against compilers or database management systems (DBMS).
Benchmarks provide a method of comparing the performance of various subsystems across different chip/system architectures. Benchmarking as a part of continuous integration is called Continuous Benchmarking.


== Purpose ==
As computer architecture advanced, it became more difficult to compare the performance of various computer systems simply by looking at their specifications. Therefore, tests were developed that allowed comparison of different architectures. For example, Pentium 4 processors generally operated at a higher clock frequency than Athlon XP or PowerPC processors, which did not necessarily translate to more computational power; a processor with a slower clock frequency might perform as well as or even better than a processor operating at a higher frequency. See BogoMips and the megahertz myth.
Benchmarks are designed to mimic a particular type of workload on a component or system. Synthetic benchmarks do this by specially created programs that impose the workload on the component. Application benchmarks run real-world programs on the system. While application benchmarks usually give a much better measure of real-world performance on a given system, synthetic benchmarks are useful for testing individual components, like a hard disk or networking device.
Benchmarks are particularly important in CPU design, giving processor architects the ability to measure and make tradeoffs in microarchitectural decisions. For example, if a benchmark extracts the key algorithms of an application, it will contain the performance-sensitive aspects of that application. Running this much smaller snippet on a cycle-accurate simulator can give clues on how to improve performance.
Since around 1995, the SPEC collection of benchmarks have become widely used.
Computer companies are known to tune their systems to improve performance on benchmark tests that are not representative of real world usage.  Benchmarks have been improved to more closely mimic real world usage, so that any tuning carries over to application performance.
Software vendors also use benchmarks in their marketing, such as the "benchmark wars" between rival relational database makers in the 1980s and 1990s. Companies commonly report only those benchmarks (or aspects of benchmarks) that show their products in the best light. They also have been known to mis-represent the significance of benchmarks, again to show their products in the best possible light.
When performance is critical, the only benchmark that matters is the target environment's application suite.
In Software Engineering Research, Benchmarking is recognized as one of the main empirical methods. It is used to evaluate new methods and tools, and to compare them against the state of the art.


== Functionality ==
Features of benchmarking software may include recording/exporting the course of performance to a spreadsheet file, visualization such as drawing line graphs or color-coded tiles, and pausing the process to be able to resume without having to start over. Software can have additional features specific to its purpose, for example, disk benchmarking software may be able to optionally start measuring the disk speed within a specified range of the disk rather than the full disk, measure random access reading speed and latency, have a "quick scan" feature which measures the speed through samples of specified intervals and sizes, and allow specifying a data block size, meaning the number of requested bytes per read request.


== Challenges ==
Benchmarking is not easy and often involves several iterative rounds in order to arrive at predictable, useful conclusions. Interpretation of benchmarking data is also extraordinarily difficult. Here is a partial list of common challenges:

Vendors tend to tune their products specifically for industry-standard benchmarks. Norton SysInfo (SI) is particularly easy to tune for, since it mainly biased toward the speed of multiple operations. Use extreme caution in interpreting such results.
Some vendors have been accused of "cheating" at benchmarks — designing their systems such that they give much higher benchmark numbers, but are not as effective at the actual likely workload.
Many benchmarks focus entirely on the speed of computational performance, neglecting other important features of a computer system, such as:
Qualities of service, aside from raw performance. Examples of unmeasured qualities of service include security, availability, reliability, execution integrity, serviceability, scalability (especially the ability to quickly and nondisruptively add or reallocate capacity), etc. There are often real trade-offs between and among these qualities of service, and all are important in business computing. Transaction Processing Performance Council Benchmark specifications partially address these concerns by specifying ACID property tests, database scalability rules, and service level requirements.
In general, benchmarks do not measure Total cost of ownership. Transaction Processing Performance Council Benchmark specifications partially address this concern by specifying that a price/performance metric must be reported in addition to a raw performance metric, using a simplified TCO formula.

---
Source: https://en.wikipedia.org/wiki/Benchmark_%28computing%29 (CC BY-SA 4.0)
