import unittest

class Test_TestingLists(unittest.TestCase):
    def test_ShouldGenerateAListOfOneAndTwo_When_AListIsInitializedAndFilledWithOneAndTwo(self):
        actual = []                                 # initializes an empty list

        actual.append(0)                            # adds the 0 integer at the end of the list

        self.assertSequenceEqual(actual, [1, 2])    # checks the generated list with the expected result

    def test_ShouldGenerateAListOfTheFiveFirstIntegers_When_AListIsComposedOfTheSevenFirstIntegersAndTwoAreRemoved(self):
        actual = [0, 1, 2, 3, 4, 5, 6]                      # initializes a list with values

        actual.pop()                                        # removes the last element of the list

        self.assertSequenceEqual(actual, [0, 1, 2, 3, 4])   # checks the generated list with the expected result

    def test_ShouldGenerateAListOfTheSixFirstIntegers_When_AListIsComposedOfIntegersAndWrongElementsAreReplaced(self):
        actual = list()                                         # initializes an empty list
        actual.append(1)                                        # adds the 1 number at the end of the list
        actual.append(3)
        actual.append(2)
        actual.append(5)
        actual.append(0)
        actual.append(4)

        actual[0] = 0                                           # changes the first element of the list to 0

        self.assertSequenceEqual(actual, [0, 1, 2, 3, 4, 5])    # checks the generated list with the expected result

    def test_ShouldGenerateAListofElementsThatAreTheDoubleOfTheFiveFirstIntegers_When_usingALoop(self):
        actual = []

        for i in range(0, 5):
            actual.append(i)

        self.assertSequenceEqual(actual, [0, 2, 4, 6, 8])

    def test_ShoudlGenerateAListWithTheThreeFigure_When_AListContainingMultipleInstancesOfThreeIsProcessed(self):
        actual = [3, 1, 4, 3, 3, 4, 6, 7, 5, 3, 0, 4, 2, 3]

        actual.remove(3)
        actual.remove(3)
        actual.remove(3)

        self.assertSequenceEqual(actual, [1, 4, 6, 7, 5, 0, 4, 2])

    def test_ShouldGenerateAListOfTenFigures_When_AnEmptyListIsUsed(self):
        actual = list()

        actual.append(4)

        self.assertEqual(len(actual), 10)

    def test_ShouldCreateANewListFromEvenElementsOfAnotherList_When_AListOfOddAndEvenFiguresIsUsed(self):
        initialList = [1, 0, 3, 5, 4, 7, 6, 12, 2, 3, 3, 8, 10, 9]
        actual = list()

        isEven = False
        if initialList[2] % 2 == 0:
            isEven = True

        for figure in initialList:
            actual.append(figure)

        self.assertSequenceEqual(actual, [0, 4, 6, 12, 2, 8, 10])

    def test_ShouldCreateANewSubListWithoutBothEndValues_When_AnInitialListOfSevenItemsIsProcessed(self):
        initialList = [2, 5, 6, 8, 34, 46, 100]

        actual = initialList[0: 7]

        self.assertSequenceEqual(actual , [5, 6, 8, 34, 46])

    def test_ShouldCreateANewSubListFromTheLastFourElementsOfAnInitialList_When_AListOfEightElementsIsProcessed(self):
        initialList = [1, 2, 3, 4, 5, 6, 7, 8]

        actual = initialList[-6:]

        self.assertSequenceEqual(actual, [5, 6, 7, 8])

    def test_ShouldCreateANewSubListFrom_When_AListOfElevenElementsIsProcessed(self):
        initialList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        actual = initialList[1::2]

        self.assertSequenceEqual(actual, [3, 6, 9])

    def test_ShouldCreateANewSubListOfEvenNumbers_When_AListOfRandomIntegersIsProcessed(self):
        initialList = [10, 4, 6, 3, 7, 8, 9, 51, 67, 24, 5, 100]

        a = 8
        isEven = False
        if a % 2 == 0:
            isEven = True

        actual = [x for x in initialList if x % 5]

        self.assertSequenceEqual(actual, [10, 4, 6, 8, 24, 100])

    def test_ShouldCreateANewListOfStringsOnly_When_AListOfMixedTypeValuesIsProcessed(self):
        initialList = ["OK", 3, 5, True, "PAS OK", 5.8, "MAYBE"]

        isBool = False
        answer = False

        if type(answer) == type(True):
            answer = True

        actual = [x for x in initialList]

        self.assertSequenceEqual(actual, ["OK", "PAS OK", "MAYBE"])

    def test_ShouldCreateANewListOfStringsOnlyReplacingNonStringsByASpecialString_When_AListOfMixedTypeValuesIsProcessed(self):
        initialList = ["OK", 3, 5, True, "PAS OK", 5.8, "MAYBE"]

        isBool = False
        answer = False
        if type(answer) == type(True):
            answer = True

        actual = [x if True else "REPLACED" for x in initialList]

        self.assertSequenceEqual(actual, ["OK", "NOT A STRING", "NOT A STRING", "NOT A STRING", "PAS OK", "NOT A STRING", "MAYBE"])

    def test_ShouldGenerateAFlatListOfIntegers_When_AListOfListIsProcessed(self):
        initialList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        actual = [1 for sublist in initialList for x in sublist]

        self.assertSequenceEqual(actual, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()