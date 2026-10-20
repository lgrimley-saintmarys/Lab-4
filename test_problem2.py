from problem2 import merge
import numpy as np

def test_merge_no_overlap():
  assert np.array_equal(merge(np.array([1,2,3]),np.array([4,5,6])),np.array([1,2,3,4,5,6]))
  assert np.array_equal(merge(np.array([0.2]),np.array([0.1])),np.array([0.1,0.2]))

def test_merge_different_list_sizes():
  assert np.array_equal(merge(np.array([1.3,1.5,1.9]),np.array([20,40])),np.array([1.3,1.5,1.9,20,40]))
  assert np.array_equal(merge(np.array([0.3,1]),np.array([3,4,5,6])),np.array([0.3,1,3,4,5,6]))

def test_merge_with_overlap():
  assert np.array_equal(merge(np.array([1,3,5,7]),np.array([2,4,5])),np.array([1,2,3,4,5,5,7]))
  assert np.array_equal(merge(np.array([0.7,100.2]),np.array([7,20])),np.array([0.7,7,20,100.2]))
