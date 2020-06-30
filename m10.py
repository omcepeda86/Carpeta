#!/usr/bin/python

import pandas as pd
from sklearn.externals import joblib
import sys
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

def valores(Year,Mileage,State,Make,Model): 

    clf = joblib.load(os.path.dirname(__file__) + '/car_regr.pkl')
    le_s1 = joblib.load(os.path.dirname(__file__) + '/le_s.pkl')
    le_m1 = joblib.load(os.path.dirname(__file__) + '/le_m.pkl')
    le_k1 = joblib.load(os.path.dirname(__file__) + '/le_k.pkl')
    
    datas = [Year,Mileage,State,Make,Model] 
    
    Year1= [Year]
    Mileage1=[Mileage]
    State1=State
    State1=[" "+ State1]
    Make1=[Make]
    Model1=[Model]
    
    Df_1=pd.DataFrame({'Year':Year1, 'Mileage':Mileage1, 'State':State1, 'Make':Make1, 'Model':Model1},index=[0])

    a= le_s1.transform(Df_1['State'])
    b= le_m1.transform(Df_1['Make'])
    c= le_k1.transform(Df_1['Model'])

    Xtest=pd.DataFrame({'Year':Year1, 'Mileage':Mileage1, 'State':a, 'Make':b, 'Model':c},index=[0])
    
    Pred = clf.predict(Xtest)
    
    #clf.predict([Year, Milage])
    
    return Pred


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Por favor ingrese el carro')
        
    else:

        url = sys.argv[1]

        p1 = predict_proba(url)
        
        print(url)
        print('Valor precio estimado: ', p1)
        