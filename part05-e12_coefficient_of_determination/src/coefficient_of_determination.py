#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep = "\t")
    x = df.loc[:,"X1":"X5"]
    y = df.loc[:,"Y"]
    reg = linear_model.LinearRegression(fit_intercept = True)
    
    # Fit the model
    reg.fit(x,y)
    # Coefficient of determination = Bestimmtheitsmaß/ Determinantenkoeffizient
    # How well do the data points fit to the model used?
    coeff_det_l = []
    coeff_det = reg.score(x,y)
    coeff_det_l.append(coeff_det)



    for i in range(len(x.columns)):
        
        x_new = x.iloc[:,i].values.reshape(-1,1)
        
        reg.fit(x_new,y)
        coeff_det = reg.score(x_new,y)
        coeff_det_l.append(coeff_det)

    return coeff_det_l

    
def main():
    coeff_determination = coefficient_of_determination()
    print(coeff_determination)
    
    for i in range(len(coeff_determination)):
        print(f"R2-score with feature(s) X{i}: {coeff_determination[i]}")
    
if __name__ == "__main__":
    main()
