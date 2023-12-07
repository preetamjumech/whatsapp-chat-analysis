import re 
import pandas as pd

def preprocess(data):
    pattern = '\[\d{1,2}:\d{1,2},\s\d{1,2}\/\d{1,2}\/\d{2,4}\]\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({"user_message":messages,"message_dates":dates})
    df['message_dates'] = pd.to_datetime(df['message_dates'], format='[%H:%M, %d/%m/%Y] ')
    users=[]
    messages = []

    for m in df["user_message"]:
        user = re.split(r':',m)[0]
        message = re.split(r':',m)[1]
        users.append(user)
        messages.append(message)

    df["users"] = users
    df["messages"] = messages
    df["dates"] = df["message_dates"]
    df.drop(["user_message","message_dates"],axis=1, inplace = True)
    
    df["year"] = df["dates"].dt.year
    df["month"] = df["dates"].dt.month_name()
    df["day"] = df["dates"].dt.day
    df["hour"] = df["dates"].dt.hour
    df["minute"] = df["dates"].dt.minute

    return df
