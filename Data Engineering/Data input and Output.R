#data1 <- read.csv("marksheet.csv")

library(readr)
marksheet <- read_csv("marksheet.csv")
View(marksheet)

install.packages("rio")
library(rio)
export(marks, "marksheet.csv")
export(marks, "marksheet.xlsx")

#########################

#Exercise: create a matrix of 5 student scores in three subject...
#create student scores by using functions,
#make sure the numbers you get are integer without decimal points
#     Math  Phys  Bio  Total  Percent
#
#Ali
#Badar
#Saif
#Total


Ali= rnorm(3,88,4)
Badar= rnorm(3,66,3)
Saif= rnorm(3,88,9)

studmatrix= rbind(Ali,Badar,Saif)
studmatrix

colnames(studmatrix) <- c('Math','Phys','Bio')

studmatrix= cbind(studmatrix, 'Total'=rowSums(studmatrix))
studmatrix

studmatrix= cbind(studmatrix, 'Percent'=studmatrix[,4]/300)
studmatrix

studmatrix= rbind(studmatrix, 'Total'=colSums(studmatrix))
studmatrix

df= data.frame(studmatrix)
df
write.csv(df,'studmatrix.csv')

#
df>edit(df)


#delete a row
df[-4,]




#find the total 
rowSums(mymatrix1)
colSums(mymatrix1)