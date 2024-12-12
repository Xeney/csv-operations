import pandas as pd

class CSVFile():
    
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.data = pd.read_csv(self.file_name)

    def create(self):
        user_object = dict()
        columns = self.data.columns.tolist()
        print("У тебя следующие параметры для заполнения:")
        print("\t", columns)
        for i in columns:
            if i == "ID":
                user_object[i] = str(self.data.iloc[-1]['ID']+1)
                continue
            user_object[i] = input(f"{i}: ")
        print(user_object)
        df = pd.DataFrame([user_object])
        df.to_csv(self.file_name, encoding='utf-8', index=False, mode='a', header=False)

    # Вывод, с фильтрацией
    # csvf.get(csvf.data['Age'] > 25)
    def get(self, filters=None) -> pd.DataFrame:
        if filters is not None and isinstance(filters, (pd.Series, pd.DataFrame)):
            return self.data[filters]
        return self.data
    

if __name__ == "__main__":
    csvf = CSVFile("./csv_operations/data.csv")
    csvf.create()
    print(csvf.get())
