import numpy as np
def get_pi_values(numberofsamples):
#Monte Carlo Experiment
	counter = 0
	for i in range(numberofsamples):
	    # Generating uniform random number in the interval [A,B]
	    A = -1 
            B = +1
	    x = (B-A)*np.random.rand() + A
	    y = (B-A)*np.random.rand() + A
	    if (x**2 + y**2) < 1:
		counter += 1
	return (4*(float(counter)/float(numberofsamples)))
pi_values=[]
numberofpi=input("Enter number of pi : ")
numberofsamples=input("Enter number of samples (X,Y) : ")
for i in range(numberofpi):
	pi_values.append(get_pi_values(numberofsamples)) #add pi_values	
print("Random sample of pi values: " + str(pi_values))

#find sample mean
sum_m = 0
for i in range(numberofpi):
	sum_m=sum_m+pi_values[i];
sample_mean=sum_m/numberofpi
print("Sample mean : %f" % sample_mean);

#find sample variance
sum_v = 0
for i in range(numberofpi):
	sum_v=pi_values[i]+sample_mean;
sample_variance=sum_v/(numberofpi-1)
print("Sample variance : %f" % sample_variance);


