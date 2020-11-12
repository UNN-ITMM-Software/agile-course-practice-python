import unittest

from bisymmetric_matrix.model.bisymmetric import BisymmetricMatrix


class TestIsSquare(unittest.TestCase):
    def test_0_size_matrix(self):
        empty_matrix = BisymmetricMatrix()
        empty_matrix.init_matrix([])
        self.assertTrue(empty_matrix.is_square())

    def test_correct_square_matrix(self):
        square_matrix = BisymmetricMatrix()
        square_matrix.init_matrix([[3, 2, 1], [4, 3, 2], [5, 4, 3]])
        self.assertTrue(square_matrix.is_square())

    def test_not_square_matrix(self):
        not_square_matrix = BisymmetricMatrix()
        not_square_matrix.init_matrix([[3, 2, 1], [4, 3, 2]])
        self.assertFalse(not_square_matrix.is_square())


class TestIsSymmetric(unittest.TestCase):
    def test_0_size_matrix(self):
        empty_matrix = BisymmetricMatrix()
        empty_matrix.init_matrix([])
        self.assertTrue(empty_matrix.is_symmetric())

    def test_correct_symmetric_matrix(self):
        symmetric_matrix = BisymmetricMatrix()
        symmetric_matrix.init_matrix([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
        self.assertTrue(symmetric_matrix.is_symmetric())

    def test_not_symmetric_matrix(self):
        not_symmetric_matrix = BisymmetricMatrix()
        not_symmetric_matrix.init_matrix([[1, 2], [1, 2]])
        self.assertFalse(not_symmetric_matrix.is_symmetric())

    def test_not_square_matrix(self):
        not_square_matrix = BisymmetricMatrix()
        not_square_matrix.init_matrix([[1, 2], [3]])
        self.assertFalse(not_square_matrix.is_symmetric())


class TestIsPersymmetric(unittest.TestCase):
    def test_0_size_matrix(self):
        empty_matrix = BisymmetricMatrix()
        empty_matrix.init_matrix([])
        self.assertTrue(empty_matrix.is_persymmetric())

    def test_correct_persymmetric_matrix(self):
        persymmetric_matrix = BisymmetricMatrix()
        persymmetric_matrix.init_matrix([[1, 2, 3], [4, 1, 2], [5, 4, 1]])
        self.assertTrue(persymmetric_matrix.is_persymmetric())

    def test_not_persymmetric_matrix(self):
        not_persymmetric_matrix = BisymmetricMatrix()
        not_persymmetric_matrix.init_matrix([[1, 2], [1, 2]])
        self.assertFalse(not_persymmetric_matrix.is_persymmetric())

    def test_not_square_matrix(self):
        not_square_matrix = BisymmetricMatrix()
        not_square_matrix.init_matrix([[1, 2], [3]])
        self.assertFalse(not_square_matrix.is_persymmetric())


class TestNecessaryCondition(unittest.TestCase):
    def test_0_size_matrix(self):
        empty_matrix = BisymmetricMatrix()
        empty_matrix.init_matrix([])
        self.assertTrue(empty_matrix.necessary_condition_for_bisymmetric())

    def test_necessary_condition_for_bisymmetric_is_met(self):
        bisymmetric_matrix = BisymmetricMatrix()
        bisymmetric_matrix.init_matrix([[1, 2, 3], [2, 4, 2], [3, 2, 1]])
        self.assertTrue(bisymmetric_matrix.necessary_condition_for_bisymmetric())

    def test_necessary_condition_for_not_bisymmetric_is_met(self):
        not_bisymmetric_matrix = BisymmetricMatrix()
        not_bisymmetric_matrix.init_matrix([[1, 2, 3], [2, 3, 2], [2, 2, 1]])
        self.assertTrue(not_bisymmetric_matrix.necessary_condition_for_bisymmetric())

    def test_necessary_condition_is_not_met(self):
        necessary_condition_is_not_met_matrix = BisymmetricMatrix()
        necessary_condition_is_not_met_matrix.init_matrix([[1, 2, 3], [4, 5, 4], [3, 2, 1]])
        self.assertFalse(necessary_condition_is_not_met_matrix.necessary_condition_for_bisymmetric())


class TestIsBisymmetric(unittest.TestCase):
    def test_0_size_matrix(self):
        empty_matrix = BisymmetricMatrix()
        empty_matrix.init_matrix([])
        self.assertTrue(empty_matrix.is_bisymmetric())

    def test_correct_bisymmetric(self):
        correct_bisymmetric_matrix = BisymmetricMatrix()
        correct_bisymmetric_matrix.init_matrix([[1, 2, 3], [2, 4, 2], [3, 2, 1]])
        self.assertTrue(correct_bisymmetric_matrix.is_bisymmetric())

    def test_necessary_condition_for_not_bisymmetric_is_met(self):
        not_bisymmetric_matrix = BisymmetricMatrix()
        not_bisymmetric_matrix.init_matrix([[1, 2, 3], [2, 3, 2], [2, 2, 1]])
        self.assertFalse(not_bisymmetric_matrix.is_bisymmetric())

    def test_necessary_condition_is_not_met(self):
        necessary_condition_is_not_met_matrix = BisymmetricMatrix()
        necessary_condition_is_not_met_matrix.init_matrix([[1, 2], [2, 3]])
        self.assertFalse(necessary_condition_is_not_met_matrix.is_bisymmetric())

    def test_not_square(self):
        not_square_matrix = BisymmetricMatrix()
        not_square_matrix.init_matrix([[1, 2, 3], [4, 5, 4]])
        self.assertFalse(not_square_matrix.is_bisymmetric())