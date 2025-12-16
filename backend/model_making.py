import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# loading the dataset
df=pd.read_csv(r"dataset\college_student_placement_dataset.csv")
# remove unneccerary column
df=df.drop(columns="College_ID")
# seperating the input and output vars

input_vars=df.iloc[:,:-1]
x=input_vars
y=df["Placement"]
#y.columns["Placement"]
# now classifying the input vars to what transformation they need 
one_hot_list=list(['Internship_Experience'])
standard_s_list=list(input_vars.drop(columns="Internship_Experience").columns)

# now preparing the column transformer 
preprocessor=ColumnTransformer(
    transformers=[("tf1",OneHotEncoder(categories=[["No","Yes"]]),one_hot_list),
                  ("tf2",StandardScaler(),standard_s_list)],
                  remainder="passthrough"
)

# now train test split 
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=4,stratify=y)

# now making the pipelines
model_pipeline=Pipeline(
    steps=[
        ("preprocessor",preprocessor),
        ("model",LogisticRegression(max_iter=1000))

    ]
)
# now train the model 
model_pipeline.fit(x_train,y_train)

#now our model is trained we will check its accuracy 

result_train = model_pipeline.predict(x_train)
result_test = model_pipeline.predict(x_test)

# accuracy 
acc_train = accuracy_score(y_train, result_train) * 100
acc_test = accuracy_score(y_test, result_test) * 100


print(f"the model accuracy from tarining data is {acc_train} %")
print(f"the model accuracy from testing data is {acc_test}")

# now exporting the model as a pickel file 

# with open('student_placement_pipeline.pkl', 'wb') as file:
#     pickle.dump(model_pipeline, file)

# print("Model trained and saved as 'student_placement_pipeline.pkl'")


































