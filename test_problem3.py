from problem3 import csv_string_to_array
import numpy as np

def test_small_example():
  assert np.array_equal(csv_string_to_array("1,2,3,4,5,6,7,8"),np.array([[1,2,3,4],[5,6,7,8]]))

string=""
for i in range(399):
  string+=str(i)+","
string+=string+str(399)

def test_full_size():
  assert np.array_equal(csv_string_to_array(string),np.arange(400))
