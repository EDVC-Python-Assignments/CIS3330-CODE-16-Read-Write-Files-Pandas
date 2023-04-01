import os,sys
import random
import pytest
from code_16 import get_mario_games
from code_16 import get_zelda_games
from code_16 import get_xbox_games



def check_if_file_exists():
    try:
        exists = os.path.exists("code_16.py")
        assert exists == True
    except:
        sys.exit()

def test_mario_games():
     check_if_file_exists()
     assert(len(get_mario_games())==14)

def test_zelda_games():
     check_if_file_exists()
     assert(len(get_zelda_games())==2)

def test_xbox_games():
    check_if_file_exists()
    assert(len(get_xbox_games())==287)