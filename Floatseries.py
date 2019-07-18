import numpy as np
import pandas as pd

#Sample data file -> hareshgundlapalli/DataScience/AZRB_Sample.csv

merch = pd.read_csv('D:\\Datasets\\AZRB.csv')

merchformatted = merch.drop(len(merch) - 1,axis=0) # Clear Null row at the bottom and assign it to a new DF.
merchformatted.columns = ["ORG", "ACCTNO", "STORENO", "STORENAME", "MERCHNO", "SALESAMT", "SALESCOUNT"]
merchformatted["SALESCOUNT"] = pd.Series(list(np.random.randint(1,1000,len(merchformatted))))

merchformatted["SALESAMT"] = pd.Series(list(np.random.uniform(0.0, 999999.99))) #This aint working because float is not iterable. Hence the below for loop.

for i in range(len(merchformatted)):
    #print(merchformatted.SALESAMT[i])
    merchformatted.iloc[[i],[5]] = round(np.random.uniform(0.0, 999999.99), 2)
    
merchformatted.SALESAMT = pd.to_numeric(merchformatted.SALESAMT) # Format SALESAMT column to numeric.    

# merchformatted.drop("SALESAMT",1,inplace=True) #Drop column

