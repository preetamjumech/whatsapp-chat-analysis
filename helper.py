from urlextract import URLExtract
from wordcloud import WordCloud
extract = URLExtract()


def fetch_stats(selected_user, df):

    if selected_user == "Overall":
        num_messages = df.shape[0]
        words=[]
        for message in df["messages"]:
            words.extend(message.split())

        num_media_msg = df[df["messages"]== '<Media imitted>\n'].shape[0]

        links = []
        for message in df["messages"]:
            links.extend(extract.find_urls(message))

        return num_messages, len(words) , num_media_msg, len(links)
    else:
         new_df = df[df["users"]== selected_user]
         num_messages = new_df.shape[0]
         words=[]
         for message in df["messages"]:
            words.extend(message.split())
         num_media_msg = new_df[new_df["messages"]== '<Media imitted>\n'].shape[0]

         links = []
         for message in new_df["messages"]:
            links.extend(extract.find_urls(message))
         return num_messages, len(words), num_media_msg, len(links)



def most_busy_users(df):
    X = df["users"].value_counts().head()
    df = round((df["users"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns = {"index":"name","users":"percent"})
    return X , df

def create_wordcloud(selected_user,df):
    if selected_user == "Overall":
        wc = WordCloud(width= 500, height=500, min_font_size=10, background_color="white")
        df_wc = wc.generate(df["messages"].str.cat(sep = " "))
        return df_wc
    else:
         new_df = df[df["users"]== selected_user]
         wc = WordCloud(width= 500, height=500, min_font_size=10, background_color="white")
         df_wc = wc.generate(new_df["messages"].str.cat(sep = " "))
         return df_wc
