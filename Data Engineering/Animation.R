# Get data:
library(gapminder)

# Charge libraries:
library(ggplot2)
library(gganimate)
#library(gifski)
#library(png)



# Make a ggplot, but add frame=year: one image per year
myPlot<- ggplot(gapminder, aes(gdpPercap, lifeExp, size = pop, color = continent)) +
  geom_point() +
  scale_x_log10() +
  theme_bw() +
  # gganimate specific bits:
  labs(title = 'Year: {frame_time}', x = 'GDP per capita', y = 'life expectancy') +
  transition_time(year) +
  ease_aes('linear')

# Save at gif:
animate(myPlot, duration = 5, fps = 20, width = 500, height = 500, renderer = gifski_renderer())
anim_save(filename = "271-ggplot2-animated-gif-chart-with-gganimate1.gif")
