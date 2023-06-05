list1=c(180,250,300,120,130,160)
list2=c(10,20,30,40,50,60)
list3=c(25,30,35,35,40,45)
mean()

#Day2
#wighted mean
(wm=c(10000*8+12000*10+8000*12)/8+10+12)
#z-score
A=c(44,39,22,50,64)
B=c(22,20,18,30,11)
zscoreA=((A-mean(A))/sd(A))
zscoreb=((B-mean(B))/sd(B))

#random
set.seed(123)
values=rnorm(100,40,2)
boxplot(values[-c(3,50)],col = "blue",horizontal = TRUE)
fivenum(values)
summary(values)

values[50]
values[50]=values[50]+40
values[50]=values[50]-30
