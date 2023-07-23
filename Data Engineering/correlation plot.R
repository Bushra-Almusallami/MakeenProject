# http://www.sthda.com/english/wiki/correlation-analyses-in-r
library(corrplot)
library(RColorBrewer)
M <-cor(mtcars)
corrplot(M, type="upper", order="hclust",
         col=brewer.pal(n=10, name="RdGy"))
#
display.brewer.all(type="div")
