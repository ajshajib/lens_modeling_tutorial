1. Think about one experiment where you toss a coin for $N_{\rm trial} = 200$ times, with each 
toss having a 50% probability for the head. In this experiment, you count the total number of heads $N_{\rm head}$. Write a Python code that gives you $N_{\rm head}$. This is a random number that should provide a different number if the experiment is run again. (This is the optional assignment from last week, but try to complete it.)
2. Now run this experiment 1000 times. Plot a histogram of the 1000 $N_{\rm head}$ values from 
   these 1000 experiments. What distribution does the histogram look like?
3. What is the mean and standard deviation of these 1000 numbers? Does it match the 
   predicted mean and standard deviation using formulae for the Binomial distribution?
4. Now, think about a coin for which the probability of a head is 0.1%. You toss the 
   coin $N_{\rm trial} = 100,000$ times for one experiment. What does the distribution look like if you repeat the experiment 1000 times? Take the mean and standard deviations of the 1000 $N_{\rm head}$ values. Do they match the predicted mean and standard deviation of the Poisson distribution?
5. Think about the average probability for one resident in Dhaka city to visit the 
   Star Kabab Restaurant between 7-8 pm. The average probability is not zero. Otherwise, the restaurant won’t have any customers, but we know they do have customers every day at that time. The number of customers between 7-8 pm for different days will be different random numbers. If you collect this number from 50 different days, what distribution would these 50 numbers follow?
6. If you have counted the number of customers between 7-8 pm to be 100 today, what is 
   the expected number and uncertainty for tomorrow 7-8 pm?
7. Try to understand these terms as much as possible, if not already: 
   1. Bayes’ theorem, 
   2. likelihood function, 
   3. prior probability distribution, and 
   4. posterior probability distribution.
8. (Optional): Read about PEP8: https://peps.python.org/pep-0008/ . This is the 
      official recommendation for writing Python code, which is very helpful when code is shared between collaborators.
