#importing dataset
library(readr)
Salary_Data <- read_csv("C:/Users/user/Desktop/Rstudio/Project1/Salary_Data.csv")
View(Salary_Data)

summary(Salary_Data)
str(Salary_Data)
#number of variables, x1=Salary_Data[,2] > View(x1)
#number of casses(observation), x2=Salary_Data[2,] > View(x2)

#view boxplot for continouse columns
par(mfrow=c(2,2))
boxplot(data1[,3],col = "pink", horizontal = TRUE, main ="Years of Experience")
boxplot(data1[,4],col = "light green",horizontal = TRUE, main ="Salary")
boxplot(`Years of Experience`~ Gender,col = "light blue", horizontal = TRUE, main ="Years of Experience")
boxplot(Salary~ Gender,col = "light blue", horizontal = TRUE)



#Fitting linear model for reading and writing scors
data1$Experience= data1$`Years of Experience`
data1$salary= data1$Salary
attach(data1)

plot(Experience,salary,col="blue")
#corellation
cor(data1$Experience,data1$salary, use="complete.obs") 

#w/o null
newdata= na.omit(data1)

model01= lm(newdata$Experience~ newdata$salary)
summary(model01)

#fitting line
abline(model01,col="green")


#create male & female sub dataset
Mdata= newdata[newdata$Gender=="Male",]
Fdata= newdata[newdata$Gender=="Female",]



############### Catigurical columns  ##################
#table
table(newdata$Gender)

#corellation between Experience and gender
cor(newdata$Experience,newdata$Gender=="Male", use="complete.obs")
cor(newdata$Experience,newdata$Gender=="Female", use="complete.obs")

#corellation between salary and gender
cor(newdata$salary,newdata$Gender=="Male", use="complete.obs")
cor(newdata$salary,newdata$Gender=="Female", use="complete.obs")

#boxplot
par(mfrow=c(1,2),col="gray")
par(bg="gray")

plot(newdata$Experience,newdata$Gender=="Male",col="blue",main ="Years of Experience")
plot(newdata$Experience,newdata$Gender=="Female",col="red",main ="Years of Experience")

plot(newdata$salary,newdata$Gender=="Male",col="blue",main ="Salary")
plot(newdata$salary,newdata$Gender=="Female",col="red",main ="Salary")

newdata$RD= (newdata(newdata$Gender-mean(newdata$Gender)))/sd(newdata$Gender)

#create bar chart
barplot(table(newdata$Gender),col=rainbow(7),main ="Gender")
barplot(table(newdata$`Education Level`),col=rainbow(7),main ="Education Level")

