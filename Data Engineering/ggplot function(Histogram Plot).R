library(ggplot2)
varnorm= as.integer(rnorm(200,4,3))
varunif= as.integer(runif(200,1,7))
Count= rnorm(200,10,5)
df= data.frame(varnorm,varunif,Count)
#
str(df)
summary(df)
#pass a column straight into hist()
hist(varnorm)

#
#
#using ggplot, lots of obility, but bit more complicated
ggplot(data= df, aes(varnorm))+geom_histogram()

#customizing gplot
qplot(data=df,x=varnorm,geom = 'histogram',xlim = c(0,15), color='red')
#
qplot(varnorm,data=df,geom = 'histogram',fill=I('blue'),alpha=0.2)
#
#ggplot(data,aesthetics)
pl <- ggplot(df, aes(x=varnorm))

pl+ geom_histogram()

pl+ geom_histogram(binwidth = 1, color='red',fill='pink')
#adding lables
pl<- ggplot(df,aes(x=varnorm))
pl+ geom_histogram(binwidth = 1, color='red',fill='pink')+ xlab('Normal Distribution')+ ylab('Occurences')+ggtitle('Histogram of Normal Distribution')

#change alpha (Transparency)
pl<- ggplot(df,aes(x=varnorm))
pl+ geom_histogram(binwidth = 1, color='red',fill='blue',alpha=0.6)+ xlab('Normal Distribution')+ ylab('Occurences')+ggtitle('Histogram of Normal Distribution')

#line types
pl<- ggplot(df,aes(x=varnorm))
pl+ geom_histogram(binwidth = 1, color='red',fill='blue',alpha=0.4,linetype='dotted')+ xlab('Normal Distribution')+ ylab('Occurences')+ggtitle('Histogram of Normal Distribution')

##Advanced aesthetics
pl<- ggplot(df,aes(x=varnorm))
pl+ geom_histogram(binwidth = 0.5, color='red',fill='blue',alpha=0.4,linetype='dotted')+ xlab('Normal Distribution')+ ylab('Occurences')+ggtitle('Histogram of Normal Distribution')

##Advanced aesthetics
pl<- ggplot(df,aes(x=varnorm))
pl+ geom_histogram(binwidth = 0.5, aes(fill=factor(varnorm)))+ xlab('Normal Distribution')+ ylab('Occurences')+ggtitle('Histogram of Normal Distribution')

######################################################

