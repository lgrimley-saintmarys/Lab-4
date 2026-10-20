from problem4 import chessboard
import numpy as np

def test_small():
  assert np.array_equal(chessboard(1),np.array([[1]]))

def test_odd():
  assert np.array_equal(chessboard(3),np.array([[1,0,1],[0,1,0],[1,0,1]]))
  assert np.array_equal(chessboard(5),np.array([[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]]))

def test_even():
  assert np.array_equal(chessboard(2),np.array([[1,0],[0,1]]))
  assert np.array_equal(chessboard(4),np.array([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]]))
