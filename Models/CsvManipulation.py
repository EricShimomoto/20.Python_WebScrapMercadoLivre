
class CsvManipulation:
    def __init__(self,df,name):
        self.df = df
        self.name = name
        
    def Save(self):
        self.df.to_csv(f'csv\\{self.name}.csv',index=False)