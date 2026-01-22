import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib 
file  = pd.read_csv(r"C:\Users\sumit\OneDrive\Pictures\Documents\Updated Quality of Life Data.csv")
frame =  pd.DataFrame(file)
label = LabelEncoder()
frame["gender"]=label.fit_transform(frame["gender"])
frame["occupation_type"]=label.fit_transform(frame["occupation_type"])
inputs = frame[["gender","occupation_type","avg_work_hours_per_day","avg_rest_hours_per_day","avg_sleep_hours_per_day",
               "avg_exercise_hours_per_day"]]
output = frame["age_at_death"]
x_train , x_test , y_train , y_test = train_test_split(inputs,output,random_state=42,train_size=0.8)
model = XGBRegressor()
model.fit(x_train,y_train)
joblib.dump(model,"model.pkl")
print(frame)

file_sec  = pd.read_csv(r"C:\Users\sumit\OneDrive\Pictures\Documents\Daily_Water_Intake.csv")
frame_sec =  pd.DataFrame(file_sec)
label_sec = LabelEncoder()
frame_sec["Gender"]=label_sec.fit_transform(frame_sec["Gender"])
frame_sec["Physical Activity Level"]=label_sec.fit_transform(frame_sec["Physical Activity Level"])
frame_sec["Weather"]=label_sec.fit_transform(frame_sec["Weather"])
frame_sec["Hydration Level"]=label_sec.fit_transform(frame_sec["Hydration Level"])


inputs_sec = frame_sec[["Age","Gender","Weight (kg)","Physical Activity Level","Weather"]]
output_sec = frame_sec["Daily Water Intake (liters)"]
x_train , x_test , y_train , y_test = train_test_split(inputs_sec,output_sec,random_state=42,train_size=0.8)
model_sec = XGBRegressor()
model_sec.fit(x_train,y_train)
joblib.dump(model_sec,"model_sec.pkl")
print(frame_sec)


file_third  = pd.read_csv(r"C:\Users\sumit\OneDrive\Pictures\Documents\Students Social Media Addiction.csv")
frame_third =  pd.DataFrame(file_third)
label_third = LabelEncoder()
frame_third["Gender"]=label_third.fit_transform(frame_third["Gender"])
frame_third["Academic_Level"]=label_third.fit_transform(frame_third["Academic_Level"])
frame_third["Most_Used_Platform"]=label_third.fit_transform(frame_third["Most_Used_Platform"])
frame_third["Affects_Academic_Performance"]=label_third.fit_transform(frame_third["Affects_Academic_Performance"])
frame_third["Relationship_Status"]=label_third.fit_transform(frame_third["Relationship_Status"])

inputs_third = frame_third[["Age","Gender","Academic_Level","Avg_Daily_Usage_Hours","Most_Used_Platform",
                          "Affects_Academic_Performance","Sleep_Hours_Per_Night","Relationship_Status"]]
output_third = frame_third[["Addicted_Score"]]
x_train , x_test , y_train , y_test = train_test_split(inputs_third,output_third,random_state=42,train_size=0.8)
model_third = XGBRegressor()
model_third.fit(x_train,y_train)
joblib.dump(model_third,"model_third.pkl")
print(frame_third) 