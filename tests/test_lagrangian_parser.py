import unittest

try:
  from openfoamparser import lagrangian_parser as lp
except:
  from Ofpp import lagrangian_parser as lp

class TestSum(unittest.TestCase):
  def test_lagrangian_parser(self):
    """
    Verify that the particle velocity vector is read correctly as
    a numpy array with 1000 rows and three columns
    """
    test_data = "tests/test_data/lagrangian_U"
    velocity = lp.parse_lagrangian_field(test_data)
    self.assertEqual(velocity.shape, (1000, 3))

  def test_lagrangian_parser_max_num_p(self):
    """
    Verify that the particle velocity vector is read correctly as
    a numpy array with 10 rows and three columns, when max number 
    of particles to read is equal to 10
    """
    test_data = "tests/test_data/lagrangian_U"
    velocity = lp.parse_lagrangian_field(test_data, max_num_p=10)
    self.assertEqual(velocity.shape, (10, 3))


if __name__ == "__main__":
  unittest.main()
