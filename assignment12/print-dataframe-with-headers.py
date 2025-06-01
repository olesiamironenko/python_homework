import pandas as pd

# Task 5: Extending a Class
# 5.2: Create a class called DFPlus. 
# It should inherit from the Pandas DataFrame class
class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus
    # 5.3: Create a from_csv class method
    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    # 5.4: Within the DFPlus class, declare a function called print_with_headers()
    def print_with_headers(self):
        # 5.5: print the whole DataFrame in a loop, printing 10 rows at a time
        for i in range(0, len(self), 10):
            print(f"\n--- Rows {i+1} to {i+10} ---")
            print(self.iloc[i:i+10].to_string(index=False))  # index=False hides row index
            i=i+10

# Main block
if __name__ == "__main__":
    # 5.6: Using the from_csv() class method, create a DFPlus instance from "../csv/products.csv".
    dfp = DFPlus.from_csv("../csv/products.csv")

    # 5.7: Use the print_with_headers() method of your DFPlus instance to print the DataFrame
    dfp.print_with_headers()