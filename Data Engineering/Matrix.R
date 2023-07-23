y <- matrix(1:20, nrow = 5, ncol = 4)
y

cells <- c(1,26,24,68)
rnames <- c('R1','R2')
cnames <- c('C1','C2')

mymatrix <- matrix(cells, nrow = 2, ncol = 2, byrow = TRUE, dimnames = list(rnames,cnames)) 
mymatrix

mymatrix <- matrix(cells, nrow = 2, ncol = 2, byrow = FALSE, dimnames = list(rnames,cnames)) 
mymatrix


colnames(mymatrix) <- cnames
cnames

rownames(mymatrix) <- rnames
rnames

mymatrix*2

mymatrix*mymatrix

########################################
#1
cells1 <- c(1,26,24,68,33,45)
rnames1 <- c('R1','R2')
cnames1 <- c('C1','C2','C3')

mymatrix1 <- matrix(cells1, nrow = 2, ncol = 3, byrow = TRUE, dimnames = list(rnames1,cnames1)) 
mymatrix1

#2
cells2 <- c(5,3,77,22,34,17)
rnames2 <- c('R1','R2','R3')
cnames2 <- c('C1','C2')

mymatrix2 <- matrix(cells2, nrow = 3, ncol = 2, byrow = TRUE, dimnames = list(rnames2,cnames2)) 
mymatrix2


install.packages("export")


#matrix1 * matrix2
mymatrix1%*%mymatrix2

#
mymatrix1[1,2]

#row2
mymatrix1[2,]
#col2
mymatrix1[,2]



