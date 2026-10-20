from problem1 import flatten
import numpy as np

def test_already_fine():
  assert np.array_equal(flatten(np.array([1,2,3,4]),np.array([1,2,3,4])))

def test_one_layer():
  assert np.array_equal(flatten(np.array([[1,2],[3,4]]),np.array([1,2,3,4])))

def test_two_layers():
  assert np.array_equal(flatten(np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])),np.array([1,2,3,4,5,6,7,8,9,10,11,12]))
