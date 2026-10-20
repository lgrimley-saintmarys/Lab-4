from problem5 import nearest
import numpy as np

def test_has_value():
  assert nearest(np.array([1,2,3,4]),3)==3
  assert nearest(np.array([23.2,52.6,0.0]),23.2)==23.2

def test_does_not_have_value():
  assert nearest(np.array([1,2,3,4]),2.3)==2
  assert nearest(np.array([23.2,52.6,0.0]),20)==23.2
