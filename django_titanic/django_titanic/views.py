from django.shortcuts import render
from . import help_modules

def home(request):
    return render(request,'index.html')
def predict(request):
    Pclass = request.GET['pclass']
    Sex = request.GET['sex']
    Age = request.GET['age']
    SibSp = request.GET['sibsp']
    Parch = request.GET['parch']
    Fare = request.GET['fare']
    Embarked = request.GET['embarked']
    Title = request.GET['title']

    prediction = help_modules.check_if_survived(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title)
    if prediction == 0:
        prediction = "Not Survived"
    elif prediction == 1:
        prediction = "You Survived"
    else :
        prediction= "Wrong input"

    return render(request,'predict.html',{'survived':prediction})
