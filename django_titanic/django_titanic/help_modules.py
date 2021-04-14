def check_if_survived(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title):
    import pickle
    x = [[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title]]
    random_forest = pickle.load(open('titanic_model.model','rb'))
    predict = random_forest.predict(x)
    return predict