# Title     : TODO
# Objective : TODO
# Created by: Lakefork15
# Created on: 8/17/20

tick1data <- read.csv(file = "/Users/Lakefork15/Desktop/stockprices.csv", header = FALSE)
tick1 <- unlist(t, use.names = FALSE)
hist(tick1)