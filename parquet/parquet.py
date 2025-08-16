import pandas as pd 

class DatasetConverter:
    def __init__(self,input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.dataframe = None

    def read_dataset(self):
        self.dataframe = pd.read_csv(self.input_path)
        return self.dataframe
    
    def convert_to_parquet(self):
        self.dataframe.to_parquet(self.output_path, engine = "pyarrow", index = False)

    def maximum(self):
         return self.dataframe.max(numeric_only=True)
    
    def minimum(self):
        return self.dataframe.min(numeric_only=True)

    def mean(self):
        return self.dataframe.mean(numeric_only=True)

    def absolute(self):
        return self.dataframe.select_dtypes(include='number').abs().max()



if __name__ == "__main__":
    input_file = "tripadvisor_review.csv"
    output_file = "tripadvisor_review.parquet"

    converter = DatasetConverter(input_file, output_file)
    converter.read_dataset()
    converter.convert_to_parquet()

    print("Maximum values: ",converter.maximum())
    print("Minimum Value: ",converter.minimum())
    print("Mean Value: ",converter.mean())
    print("Absolute Value: ",converter.absolute())


    


