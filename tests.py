#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 22

def test_code():
    assert main.deadEnd([0,0]) == [0, 'dead'], "deadEnd([0,0]) == [0, 'dead'] failed"
    assert main.deadEnd([10,10,4,3,2,4,6,3,3,53,4]) == [10,10,4,3,2,4,6,3,3,53,'dead'], "main.deadEnd([10,10,4,3,2,4,6,3,3,53,4]) == [10,10,4,3,2,4,6,3,3,53,'dead']"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
