# coding=utf-8
import numpy


def DFLCS(strA, strB):
    lengA = len(strA)
    lengB = len(strB)
    common = numpy.zeros((lengA, lengB))  # matrix to hold the length of the common str
    cLen = 0  # length of the longest common string
    endIndexA = -1  # endIndex of the longest common string in string A

    for indexA, charA in enumerate(strA):
        for indexB, charB in enumerate(strB):
            if charA == charB:
                if indexA == 0 or indexB == 0:
                    common[indexA][indexB] = 1
                else:
                    common[indexA][indexB] = common[indexA - 1][indexB - 1] + 1

                if common[indexA][indexB] > cLen:
                    cLen = common[indexA][indexB]
                    endIndexA = indexA
            else:
                common[indexA][indexB] = 0
    return (cLen, endIndexA)


# print DFLCS('a123c4b', 'c123c4d')
