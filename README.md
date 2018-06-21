# NEAT_Tester
Automated Software Tester using NEAT Algorithm
---
This repository impliments the algorithm in [this paper](https://github.com/hlpr98/NEAT_Tester/blob/master/The%20Paper.pdf).

## Running the software

* Clone this repository
* For running the tester copy paste the following lines in the terminal.
```
$ cd NEAT_Tester
$ python ./TestingApp/generate_test.py
$ python Final_Product.py
```
* The final, optimised test suite will be in the file File_test_suite.py

## Training

- The repository already contains a trained network, stored as "winner.pkl".
- In order to train the network.<br>
  * Make changes in the "config" file.
  * Make changes in "NEAT_train.py"
  * Run "NEAT_train.py".


