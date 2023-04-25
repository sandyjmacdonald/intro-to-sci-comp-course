#!/usr/bin/env Rscript

# The tidyverse library includes the ggplot plotting library.
library(tidyverse)

# Set up command line arguments, so that we can pass the input and output file
# names in to this R script.
args = commandArgs(trailingOnly=TRUE)

# Print a warning if no arguments are supplied, and set a default output name
# if only one argument (i.e. the input file name) is supplied.
if (length(args)==0) {
  stop("At least one argument must be supplied (input file)", call.=FALSE)
} else if (length(args)==1) {
  args[2] = "weather-data-plot.jpg"
}

# read the CSV file with the data into a dataframe.
df = read.csv(args[1], header=TRUE)

# Convert the date string to a proper date class.
df$date = as.Date(df$date, format='%Y-%m-%d')

# Plot the temperature vs. the date as a scatter plot, with a line fitted to
# the points using ggplot's stat_smooth function.
p = ggplot(data=df, aes(x=date, y=temperature)) + 
  geom_point(aes(colour="red")) + 
  stat_smooth(se=FALSE, method="loess", span=0.4, colour="black") +
  theme_minimal(base_size=14) +
  xlab("Month") +
  ylab("Temperature (°C)") +
  theme(legend.position="none", plot.title=element_text(hjust=0.5)) +
  ggtitle("Daily mean temperature")

# Save the plot to the file name specified in the arguments.
ggsave(args[2], plot=p, bg="white", height=6, width=6)