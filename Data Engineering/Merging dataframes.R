df1 <- data.frame(c('ID','Name','Perc'))
df1 <- edit(df1)
df2 <- edit(df2)
df1 <- data.frame(cbind('ID','Name','Percent'))
View(df1)
View(df2)
df2= data.frame(cbind('ID'=5))
df2= data.frame(cbind('ID'=2,'Status'='Enrolled','Year'=4))

#####################
#Another way
#df1
ID1 =c(1:3)
Name= c('Ali','Bader','Saif')
Perc=c(87,56,77)
df1=data.frame('ID'=ID1,'Name'=Name,'Percent'=Perc)
(df1)

#df2
df2= data.frame('ID'=c(2:5),'Status'=c('Grd','Grd','Enr','Enr'),'Year'=c(3,5,2,1))
View(df2)

#Merging Data Frames
total <- merge(df1,df2,by='ID')
View(total)

################# Home Work #####################
#Try to find other ways
#You may notice the merging produces only the matched rows
#try to find a way that have all record but without duplicate records




