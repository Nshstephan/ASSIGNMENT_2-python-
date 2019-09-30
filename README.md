# How to use

/* execute main.py*/


The script will automatically create the folders `./files` and 
`./files_new` if those doesn't exist. Then the files will be moved from one directory
 to another and back by the 3 different ways.


# Benchmark
Sice test was done on virtual machine (~20% of actual laptops power), results are slower than on host OS.

| Method                     | Average duration  |
| -------------------------- | ----------------- |
| Synchronously moving files | 28.16639 Seconds  |
| ProcessingApp              | 20.55649 Seconds  |
| ThreadingApp               | 26.409828 Seconds |



