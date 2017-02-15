Introduction
============

Welcome! This package has several Python programs implementing the state estimation algorithm described in the following paper:

**Towards Optimal State Estimation of Switched Nonlinear Systems with finite-data-rate measurements** by *Hussein Sibai* and *Sayan Mitra* to appear in
the International Conference on Hybrid Systems:Computation and Control, 2017.

It is being made available primarily for the purposes of checking reproducibility of the reported results. 
That said, the inputs to the algorithm are generated randomly in the last experiment, so, exact reproduction is unlikely!


## Quick summary:
* A program for creating hyperrectangles and gridding rectangles
* Simulating dynamical systems
* Estimating the state of a switched dynamical system with unknown switching signal
* Plotting state estimation algorithm in action

## Setup 
* Not much to setup. Just download and run the scripts. I am using python 2.7.10. estimate_switched.py is the main file. I am using Macbook Pro, OS X Yosemite, 2 GHz Intel Core i7 processor and 16 GB 1600 MHz DDR3 memory. However, it these files can be run on any machine that has python and the packages below.

## Dependencies
1. Control package of python 
2. Numpy, Scypy, Matplotlib, slycot, scipy, math and several other standard packages


To reproduce the Figure 2 exactly, go to estimate_switched.py at the end of the file and uncomment the code line for one of the subfigures to reproduce it. Everything is explained in the comments there.

To reproduce a similar table to that of the one at the end of the paper, uncomment the last part of the code. It is generated randomly, so exact reproduction is unlikely for this one. 
