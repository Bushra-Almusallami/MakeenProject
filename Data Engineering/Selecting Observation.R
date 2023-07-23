mydata= data.frame(Titanic)
View(mydata)
head((mydata))

#Selecting Observation
newdata <-mydata[which(mydata$Class=='Crew' & mydata$Survived=='Yes'),]
View(newdata)

#the subset() function
newdata <- subset(mydata,age >= 35 | age <24, select = c(q1))
newdata <- subset(mydata,mydata$Class=='Crew' & mydata$Survived=='Yes', select = c(Class,Survived))

newdata <- subset(leadership)

#################################
mydata1= data.frame(cars)
View(mydata1)

newdata <-subset(mydata1,speed >=10 | dist >=10 & dist <20, select = c(speed,dist))
View(newdata)

############################
mydata1= data.frame(BOD)
View(mydata1)

#random samples
mysample <- BOD[sample(1:nrow(BOD),5, replace = TRUE),]  #replace either false or true
View(mysample)

#using sql statement to manipulate data frame
library(sqldf)
newdf <- sqldf("select * from cars where speed=20 order by dist DESC", row.names = FALSE)
View(newdf)
