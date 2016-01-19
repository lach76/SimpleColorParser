#!/usr/bin/python
"""
    Simple Color Parser for Specific Test File


"""

class SimpleParser(object):
    BaseList = [30, 40]     # foreground / background
    ColorList = [0, 1, 2, 3, 4, 5, 6, 7]    # Colors : Black, Red, Green, Yellow, Blue, Magenta, Cyan, White

    ReplaceDict = {}

    def __init__(self):
        self.makeReplaceDict()
        pass

    def makeReplaceDict(self):
        _BaseList = ['FG', 'BG']
        _ColorList = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']

        for baseindex, base in enumerate(_BaseList):
            for colorindex, color in enumerate(_ColorList):
                colorString = "%s.%s" % (base.upper(), color.upper())
                self.ReplaceDict[colorString] = '\033[1;%sm' % (self.BaseList[baseindex]+ self.ColorList[colorindex])

        self.ReplaceDict['DEF'] = '\033[1;m'
        pass

    def parserString(self, input):
        output = input
        for colorKey, colorValue in self.ReplaceDict.items():
            key = '[%s]' % colorKey
            output = output.replace(key, colorValue)

        return output

    def parserStrings(self, inputs):
        outputs = []
        for input in inputs:
            outputs.append(self.parserString(input))

        return outputs

    def printFile(self, filename):
        with open(filename, "r") as readfile:
            lines = readfile.readlines()

        outputlines = self.parserStrings(lines)
       
        import sys
        for line in outputlines:
            sys.stdout.write(line)

if __name__ == '__main__':
    parser = SimpleParser()
    parser.printFile("../Scanner/OSSLicenseGuide.txt")

