#!/usr/bin/env python

from pathlib import Path
import os

class Config:
    """ contains configuration details about the project """
    
    # file paths
    ROOT = Path( Path.cwd().resolve() )
    RAW = Path( ROOT / 'data' / 'raw' ).as_posix()
    PREPROCESSED = Path( ROOT / 'data' / 'preprocessed' ).as_posix()
    SUBMISSION = Path(ROOT / 'data' / "submission" ).as_posix()
    MODELS = Path( ROOT / 'models' ).as_posix()
    REPORTS =  Path(ROOT / "reports" ).as_posix()
    CLEANED_TRAIN =  Path( ROOT / 'data' / 'preprocessed' / 'train.csv' ).as_posix()
    CLEANED_TEST =  Path( ROOT / 'data' / 'preprocessed' / 'test.csv' ).as_posix()
    FILE_META = Path(ROOT / "reports" / 'file_meta.csv' ).as_posix()
    # data configs
    TARGET = 'target'
    ID = 'id'

    # model configs
    seed = 42
    verbose = None
    n_estimators = 10000

    


