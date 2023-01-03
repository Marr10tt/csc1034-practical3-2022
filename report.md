# CS1034 Assessment 3
----------------------
## Baseline information
* stochastic algorithm time - 213.41 seconds
* distributive algorithm time - 0.03 seconds
----------------------
## methods of optimisation to try
* memoisation
* numpy loops instead of default python loops
-----------------------
# memoisation
I saw that memoisation could be used to optimise python code, as a result i began implementing this, it is a method which is used to help speed up functions. When i began further research i found that it was mostly usually used for recursive functions, though it is also generally helpful as it allows for variables and values to be cached, and thus more quickly accessed and used within a function.
-----------------------
# numpy loops instead of default python loops
Though this seemed promising as i saw many examples of using numpy to optimise loops and code, though most of these only applied to specific mathematical equations and scenarios, many of which i wasnt using, meaning that it was overall not feasible to implement this in my code.
-----------------------
# multithreading the stochastic function
multithreading is where code is split up and each section is given to a specific 'thread', these threads share memory and data space but are each individually computed, this (i believe) will be able to speed my code up reasonably easily by splitting my stochastic function up into 4 sets of crawlers, each handled by an individual thread. 

after implementing multi-threading, i have successfully cut down my time for the stochastic algorithm drastically. this is as i am calculating 8 smaller functions consecutively, as a reult, accuracy may suffer occasionally.
------------------------
## final results
* Stochastic algorithm ≈ 9-11 seconds
* distributive algorithm - 0.02 seconds