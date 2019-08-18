# Assignment on Logistic Regression - Dummy Variables
# Created on 08/18/2019
# Purpose: Create Dummy variables on categorical variable and perform EDA
#For Credit Data worksheet,
#Cleans Data - Checks for Nulls and NA and fills them with Mode / Mean of the variable depending on its type.
#Create Dummy variables - for all categorical variables in the dataframe.
#Delete original, non inclusive dummy variables

#Pending: Correcting custom function for data cleanup when variable is supplied, data correlation between variables.

#to get mode of a factor variable
getmode <- function(v) {
  temp <- table(as.vector(v)) #as.vector converts nXn matrix to a vector and table creates the counts for each unique values in the list
  names(temp)[temp == max(temp)] #names function returns the names of the 1st row of the table which is considered as column header and the [] requires the value part which is the maximum of the list / vector supplied which here is v.
}

#Data cleanup - to convert all blanks to the mode of each variable in the dataset
#Function need to be worked upon, throwing run errors.
fillmode <- function(var1, mode1){
  var1 <- as.factor(var1)
  var1[var1 == ""] <- mode1
  var1 <- as.factor(var1)
}

library(readr)
original <- read.csv(file.choose())
credit <- original
summary(credit)
str(credit) # STR is much better to find out the factor variables in a dataset than summary
attach(credit) 
# display how many categories each factor variable is split into
levels(Gender) #"","Female","Male"
sum(is.na(Gender)) # 0

#fillmode(credit$Married, "Yes")

#fillup Gender variable with mode(Gender)
credit$Gender <- as.character(credit$Gender)
credit$Gender[credit$Gender == ""] <- getmode(Gender)
credit$Gender <- as.factor(credit$Gender)
str(credit)

#fillup Married variable with mode(Married)
credit$Married <- as.character(credit$Married)
credit$Married[credit$Married == ""] <- getmode(Married)
credit$Married <- as.factor(credit$Married)
str(credit)

# Dependents
credit$Dependents <- as.character(credit$Dependents)
credit$Dependents[credit$Dependents == ""] <- getmode(Dependents)
credit$Dependents <- as.factor(credit$Dependents)
str(credit)

#Self_Employed
credit$Self_Employed <- as.character(credit$Self_Employed)
credit$Self_Employed[credit$Self_Employed == ""] <- getmode(Self_Employed)
credit$Self_Employed <- as.factor(credit$Self_Employed)
str(credit)

#LoanAmount
credit$LoanAmount[is.na(credit$LoanAmount)] <- as.integer(mean(LoanAmount[!is.na(LoanAmount)]))
str(credit)

#Loan_Amount_Term
credit$Loan_Amount_Term[is.na(credit$Loan_Amount_Term)] <- as.integer(mean(Loan_Amount_Term[!is.na(Loan_Amount_Term)]))
str(credit)

#Credit_History
credit$Credit_History[is.na(credit$Credit_History)] <- as.integer(mean(Credit_History[!is.na(Credit_History)]))
str(credit)

#By this time, the data is completely cleaned without any NA / blanks. Ready for further EDA

write.csv(credit,file="updated_credit_data.csv", row.names = FALSE) #Take a backup
getwd()

#Now creating dummy variables
library(dummies)
#Gender
credit2 <- credit # Copies to an internal dataset as we modify the variables
attach(credit2)

credit2 <- cbind(credit2, dummy(Gender, verbose = TRUE, sep="_"))
credit2 <- cbind(credit2, dummy(Married, verbose = TRUE, sep="_Married_"))
credit2 <- cbind(credit2, dummy(Dependents, verbose = TRUE, sep="_Dependents_"))
credit2 <- cbind(credit2, dummy(Education, verbose = TRUE, sep="_Education_"))
credit2 <- cbind(credit2, dummy(Self_Employed, verbose = TRUE, sep="_Self_Employed_"))
credit2 <- cbind(credit2, dummy(Property_Area, verbose = TRUE, sep="_Property_Area_"))
credit2 <- cbind(credit2, dummy(Loan_Status, verbose = TRUE, sep="_Loan_Status_"))
names(credit2)[names(credit2) == "credit2_Dependents_3+"] <- "credit2_Dependents_3"
names(credit2)[names(credit2) == "credit2_Education_Not Graduate"] <- "credit2_Education_Not_Graduate"
attach(credit2)
#dropping unwanted dummy variables to cleanup the dataframe

credit2 <- subset(credit2, select = -c(credit2_Female, 
                                       credit2_Married_No, 
                                       credit2_Dependents_3,
                                       credit2_Education_Not_Graduate,
                                       credit2_Self_Employed_No,
                                       credit2_Property_Area_Rural,
                                       credit2_Loan_Status_N,
                                       Loan_ID,
                                       Gender,
                                       Married,
                                       Dependents,
                                       Education,
                                       Self_Employed,
                                       Property_Area,
                                       Loan_Status
                                       ))
str(credit2)

