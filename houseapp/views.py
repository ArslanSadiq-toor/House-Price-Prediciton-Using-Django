from .forms import HouseForm 
from .models import HouseData
import joblib
import json 
import numpy as np 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 
# Create your views here.

# def indexApp(request):
# 
    # return render(request, 'index.html')



def status(df):
    try:
        model=joblib.load("random_forest_model.pkl")
        print('df',df)
        X =  np.reshape(df,(1,-1))
        print('X',X)
        y_pred = model.predict(X) 
        print('my predicion',y_pred)
        # y_pred=(y_pred>0.80) 
        # result = "Yes" if y_pred else "No"
        return y_pred 
    except ValueError as e: 
        return e 

def indexApp(request):
    if request.method=='POST':
        form=HouseForm(request.POST or None)
        if form.is_valid():
        #     Gender = form.cleaned_data['gender']
        #     Age = form.cleaned_data['age']
        #     EstimatedSalary = form.cleaned_data['salary']
        #     df=pd.DataFrame({'gender':[Gender], 'age':[Age], 'salary':[EstimatedSalary]})
        #     df["gender"] = 1 if "male" else 2
            df = [0,1,0,1,2,234,342]
            X =  np.reshape(df,(1,-1))
            # print('X',X)
            result = status(X)
            print(result)
            return render(request, 'status.html', {"data": result}) 
            
    form=HouseForm()
    return render(request, 'index.html', {'form':form})