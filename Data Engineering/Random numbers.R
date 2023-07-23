#Create a list of random numbers:
#using runif function:
#
#
#generate 10 random values from uniform distribution rounded to one decimal place
round(runif(n=10,min = 50,max = 100))


#generate 10 random values from uniform distribution
random_values1 <- round(runif(n=10,min = 50,max = 100))
var1= as.integer(random_values1)
hist(var1)

#using rnorm function
random_values2 <- rnorm(n=100,mean=10, sd=2)
var2= as.integer(random_values2)
hist(var2)
