# Libraries
library(tidyverse)
library(hrbrthemes)
library(viridis)

# create a dataset
data <- data.frame(
  name=c( rep("A",500), rep("B",500), rep("B",500), rep("C",20), rep('D', 100)  ),
  value=c( rnorm(500, 10, 5), rnorm(500, 13, 1), rnorm(500, 18, 1), rnorm(20, 25, 4), rnorm(100, 12, 1) )
)

# Plot
data %>%
  ggplot( aes(x=name, y=value, fill=name)) +
  geom_boxplot() +
  +scale_fill_viridis(discrete = TRUE, alpha=0.6) +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  theme_ipsum() +
  theme(
    legend.position="none",
    plot.title = element_text(size=11)
  ) +
  ggtitle("A boxplot with jitter") +
  xlab("")

#######################################################

#######################################################
# Boxplot basic
data %>%
  ggplot( aes(x=name, y=value, fill=name)) +
  geom_boxplot() +
  scale_fill_viridis(discrete = TRUE, alpha=0.6, option="A") +
  theme_ipsum() +
  theme(
    legend.position="none",
    plot.title = element_text(size=11)
  ) +
  ggtitle("Basic boxplot") +
  xlab("")

# Violin basic
data %>%
  ggplot( aes(x=name, y=value, fill=name)) +
  geom_violin() +
  scale_fill_viridis(discrete = TRUE, alpha=0.6, option="A") +
  theme_ipsum() +
  theme(
    legend.position="none",
    plot.title = element_text(size=11)
  ) +
  ggtitle("Violin chart") +
  xlab("")

###################################################
#
library( rgl )
library(magick)

# Let's use the iris dataset
# iris

# This is ugly
colors <- c("royalblue1", "darkcyan", "oldlace")
iris$color <- colors[ as.numeric( as.factor(iris$Species) ) ]

# Static chart
plot3d( iris[,1], iris[,2], iris[,3], col = iris$color, type = "s", radius = .2 )

# We can indicate the axis and the rotation velocity
play3d( spin3d( axis = c(0, 0, 1), rpm = 20), duration = 10 )

# Save like gif
movie3d(
  movie="3dAnimatedScatterplot", 
  spin3d( axis = c(0, 0, 1), rpm = 7),
  duration = 10, 
  dir = "~/Desktop",
  type = "gif", 
  clean = TRUE
)