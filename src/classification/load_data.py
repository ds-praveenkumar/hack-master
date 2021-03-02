# loads data from the data forlder for preprocessing

from config import Config

from pathlib import Path
import pandas as pd 
import numpy as np 


class CsvReader:
    """  reads csv from the raw folder """
    
    def __init__( self,  ):
        
        self.raw = Path( Config.RAW )
        self.preprocessed = Path( Config.PREPROCESSED )
        self.train = pd.DataFrame()
        self.test = pd.DataFrame()
        self.sub = pd.DataFrame()
        self.cleaned_train = pd.DataFrame()
        self.cleaned_test = pd.DataFrame()

    def read_csv( self, return_df= False  ):
        """ Reads csv files from raw folder """
        
        path_list = list( self.raw.glob( '*.csv' ) )
        
        for file in path_list:
            try:
                if str(file.name).startswith( 'train' ):
                    self.train = pd.read_csv( str( file ) )
                elif str( file.name ).startswith( 'test' ):
                    self.test = pd.read_csv( str( file) )
                else:
                    self.sub = pd.read_csv( str( file ) )
                print( f'>>> train size: {self.train.shape}\ttest size: {self.test.shape} <<<' )
            except Exception as e:
                print( f'exception occured at file {__name__}: {e} ' )  
            print(f"loading train data done ...", end='\n')
        if return_df:
            return self.train, self.test, self.sub

    def load_cleaned(self):
        """ loads cleaned data """

        path_list = list( self.preprocessed.glob( '*.csv' ) )
        print(self.preprocessed)
        for file in path_list:
            print( str(file))
            try:
                if str(file.name).startswith( 'train' ):
                    self.cleaned_train = pd.read_csv( str( file ) )
                    print(file)
                elif str( file.name ).startswith( 'test' ):
                    self.cleaned_test = pd.read_csv( str( file) )
            except Exception as e:
                print( f'exception occured at file {__name__}: {e} ' ) 
        print(f' { self.cleaned_train.shape }' )
        print(f"cleaned data loaded...", end='\n')


if __name__ == '__main__':
    load_csv = CsvReader()
    load_csv.read_csv( )
    load_csv.load_cleaned()