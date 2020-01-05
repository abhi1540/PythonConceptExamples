class MyData:
    def __init__(self, data):
        "Initialize MyData from a sequence"
        self.data = data

    @classmethod
    def fromfilename(cls, filename):
        "Initialize MyData from a file"
        data = open(filename).readlines()
        return cls(data)

    @classmethod
    def fromdict(cls, datadict):
        "Initialize MyData from a dict's items"
        return cls(datadict.items())


# MyData([1, 2, 3]).data

# MyData.fromfilename("/tmp/foobar").data

#MyData.fromdict({"spam": "ham"}).data