import pandas as pd
import numpy as np
import os

class CopyData:

    #This directory
    this_dir = os.path.dirname(__file__ )

    #Raw data directory
    input_dir = os.path.abspath(os.path.join(this_dir,'../../data/raw'))

    #Processed data directory
    output_dir = os.path.abspath(os.path.join(this_dir,'../../data/processed'))


    def copy_raw_to_processed(self):
        '''
        Func: Copies .csv files from one folder to another folder
        Args:
            input_dir -- input directory containing raw .csv files
            output_dir -- output directory where copied .csv files will be placed
        '''
        for file_name in os.listdir(self.input_dir):
            os.chdir(self.input_dir)
            if '.csv' in file_name:
                print(file_name)
                df = pd.read_csv(file_name)
                os.chdir(self.output_dir)
                df.to_csv(file_name)
            else:
                pass

        print('Raw data copied from {self.input_dir} to {self.output_dir}')



def main():
    CopyData().copy_raw_to_processed()

if __name__ == '__main__':
    main()
