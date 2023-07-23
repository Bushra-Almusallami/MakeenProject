#Day 1 coding
x <- 'r'
class (x)
x= c('r','t')
x1=c(3,5,45)
c(TRUE,FALSE) -> x2

#################

temp =c(34,54,23,76,78,89,3)
temp

names(temp) =c('Su','Mo','Tu','We','Th','Fr','Sa')

temp[c(3,6)]


sqrt(temp)

temp[temp>80 & temp<90]

temp70 = temp[temp != (temp>69 & temp<80)]
temp70

temp70 = temp[temp <70 | temp >79]
temp70

temp['Tu']

mean(temp)

var1=c(3,4,5)
var1[-2]
var1

#########################
temp01= temp[names(temp)%in% c('Mo','Tu')]
temp01

temp01= temp[!names(temp)%in% c('Mo','Tu')]
temp01

##########################
#practice

#1
2^5

#2

stock.price <- c(23,27,23,21,34)

names(stock.price) =c('Mon','Tues','Wed','Thu','Fri')

#3
mean(stock.price)

#
stock.price[stock.price>23]

#
max(stock.price)
stock.price[stock.price==max(stock.price)]

#
names(stock.price[stock.price==max(stock.price)])

##############################