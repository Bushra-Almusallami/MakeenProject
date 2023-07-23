library('ggplot2')
df <- mtcars
#
qplot(wt,mpg,data=df)
#
qplot(wt,mpg,data=df,color=cyl)
#
qplot(wt,mpg,data=df,size=cyl)
#
qplot(wt,mpg,data=df,size=cyl,color=cyl)
#
qplot(wt,mpg,data=df,size=cyl,color=hp,alpha=0.6)
#
pl <- ggplot(data = df,aes(x=wt,y=mpg))
pl+ geom_point()
#
pl <- ggplot(data = df,aes(x=wt,y=mpg))
pl+ geom_point(aes(color=cyl))
#
pl <- ggplot(data = df,aes(x=wt,y=mpg))
pl+ geom_point(aes(shape=factor(cyl),color=cyl))


data <- data.frame(mtcars)
data
# Plot
data %>%
  ggplot( aes(x=vs, y=mpg, fill=vs)) +
  geom_boxplot() +
  scale_fill_viridis(discrete = TRUE, alpha=0.6) +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  theme_ipsum() +
  theme(
    legend.position="none",
    plot.title = element_text(size=11)
  ) +
  ggtitle("A boxplot with jitter") +
  xlab("")