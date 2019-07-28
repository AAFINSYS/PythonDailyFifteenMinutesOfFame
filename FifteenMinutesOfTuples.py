import unittest

class TestManupulatingTuples(unittest.TestCase):
    def test_should_assert_different_tuples_but_same_components_when_two_different_tuples_with_same_composition_are_compared(self):
        first_tuple = (1, "tuple")
        second_tuple = (1, "tuple")

        self.assertNotEqual(id(first_tuple), id(second_tuple))
        self.assertEqual(first_tuple, second_tuple)

    def test_should_return_each_tuple_component_when_unpacking_a_tuple(self):
        tupleToUnpack = (1, "PythonTuple", 5.67)

        firstComponent = 0
        secondComponent = "------"
        thirdComponent = 0.0

        firstComponent, secondComponent, thirdComponent = tupleToUnpack

        self.assertEqual(firstComponent, 1)
        self.assertEqual(secondComponent, "PythonTuple")
        self.assertEqual(thirdComponent, 5.67)


if __name__ == "__main__":
    unittest.main()