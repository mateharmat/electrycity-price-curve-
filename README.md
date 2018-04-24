# electrycity-price-curve-
 I wrote my Bsc thesis about "Electricity price curve scenario generation". I've written a program code which helped with the generating part. It is written in Python. The dataset is loaded from an Excel table, and the code can be started from the Excel as well.
Short description for the files:
Price Curve optimization
	text files: Contain the values from global optimization for faster running
	root:
	-The location of the file.
	optim:
	-Loading the dataset 
	-variable declaration
	-calling functions
	-global optimization
	-plotting
lib:
	calc.py:
	-parameter (S, Sx,...,Sxy, a, sde, Kappa, Sigma) calculation for calibration
	eh.py:
	-for writing the global optimization resulsts 
	kalibration.py:
	-S stochastic process calibration
	-calibration of logPrice and Price from S process and season 
	plothelper.py:
	-helps plotting given Prices and calibrated prices 
	pred.py:
	-S stochastic process prediction for 7 days
	-Price prediction for 7 days
	predplot.py:
	-helps plotting given and predicted prices 
	randopt.py:
	-generate random starting coordinates(x_i) 
	-optimization from the x_i starting points
	readwrite.py:
	-read values from the Adatok Excel file
	-write results back in the Excel file

resources:
	Adatok.xlms:
	-contains the Prices and the [0,1] values for holiday
	-the program can be started by "clicking" optimalizálás button

test:
	allfunctiontest.py:
	-testing all the callable functions in one module
-I generated random values and calculated with them in the test part.
-Tested every function (from lib) one-by-one
