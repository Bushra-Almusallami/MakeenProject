temp <- 79.5
if(temp >= 90 & temp <= 100){
  print('A')
}else if(temp >= 80 & temp <= 89){
  print('B')
}else if(temp >= 70 & temp <= 79){
  print('C')
}else if(temp >= 60 & temp <= 69){
  print('D')
}else if(temp >= 50 & temp <= 59){
  print('E')
}else{
  print('F')
}
#################################
grade <- 102
if(grade <= 100 & grade >89){
  print('A')
}else if(grade <= 89 & grade > 79){
  print('B')
}else if(grade <= 79 & grade > 69){
  print('C')
}else if(grade <= 69 & grade > 59){
  print('D')
}else if(grade <= 59 & grade > 49){
  print('E')
}else{
  print('F')
}

###################################
a= as.integer(readline(prompt = "Enter first number: "))
b= as.integer(readline(prompt = "Enter second number: "))
s=a
sum=0
while (s<=b) {
  sum= sum+s
  s=s+1
}
print(paste("Sum is",sum))
#####################################
n= as.integer(readline(prompt = "Enter number or 999 to stop: "))
sum=0
item=0
while (n != 999) {
  sum=sum+n
  item=item+1
  n= as.integer(readline(prompt = "Enter number or 999 to stop: "))
}
#####################################

mat <- matrix(1:25, nrow = 5)
mat
#
for (i in mat) {
  print(i)
}
#
for (row in 1:nrow(mat)) {
  for (col in 1:ncol(mat)) {
    print(paste("The element at row:", row,' and col:',col,"is",mat[row,col]))
  }
}
################ Function ########################
add_num <- function(num1,num2){
  print(num1+num2)
}
add_num(4,5)
##################
hello_someone <- function(name='Frankie'){
  print(paste('Hello',))
}

###################
r<- c(10,22,45,3,14)

f<- function(r) {
  z1 <- mean(r)
  z3 <- sd(r)
  return(list(mean=z1, sd=z3))
}
b<-f(r)
b


