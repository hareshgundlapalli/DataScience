# Assignment on Multiple Linear Regression - Dummy Variables
# Created on 08/14/2019
# Purpose: Create Dummy variables on categorical variable
# Dataset: iris [builtin r]
# 3 categories

iris1 <- iris # Copies to an internal dataset iris1 to work on the dataset
summary(iris1)
attach(iris1) #Petal.Length, Petal.Width, Sepal.Length, Sepal.Width, Species
levels(Species) # display how many categories this variable is split into
table(is.na(Species)) # making sure there are no NA values in the categories


#Create new variables under iris1. We need 2 as there are 3 categories of Species
#variable if Xa == 1, its setosa and Xb == 1, its versicolor, if Xa == Xb == 0, its virginica
#Option 1 using for and if
for (i in 1:length(Species))
  {
  iris1$Xa[i] <- ifelse(Species[i] == "setosa", 1, 0)
  iris1$Xb[i] <- ifelse(Species[i] == "versicolor", 1, 0)
  #print(Species[i])
  }
str(iris1)

#Option 2 using cbind and dummies
#install.packages("dummies")
iris1 <- iris # Copies to an internal dataset iris1 to work on the dataset
library(dummies)
iris1 <- cbind(iris1, dummy(Species, verbose = TRUE))
str(iris1)

## To download the builtin datasets for external usage

write.csv(iris,file="iris.csv", row.names = FALSE)
getwd()
