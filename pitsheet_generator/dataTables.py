class dataTables:
    def __init__(self):
        self.table = {}

    def writeNew(self, tag, value):
        self.table += {tag: value}

    def getVal(self, tag):
        try:
            return self.table[tag]
        finally:
            print("no values for tag")
