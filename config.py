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

    # data configs
    TARGET = 'Response'
    


