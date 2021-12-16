import pandas as pd


class TelegramChat:

    def __init__(self,name,json_file):

        df = pd.read_json(str(json_file))['messages'].to_json('messages_data.json')

        self.name = name
        self.json_file = json_file
        self.messages_df =  pd.read_json('messages_data.json').T
        self.name_df = self.messages_df[self.messages_df['from'] == str(name)]
        self.member_name = self.messages_df['from'].unique()
        self.number_of_messages = self.name_df.shape[0]

    def get_link(self):

        for i in self.name_df.text:
            if isinstance(i,list):
                for j in i:
                    if isinstance(j,dict) and 'http' in j['text']:
                        print(j['text'])

    def get_messages(self):
        for i in self.name_df.text:
            if not isinstance(i,list):
                print(i)

    def top_ten(self):
        print(self.messages_df.groupby('from')['type'].count().sort_values(ascending=False)[:10])


