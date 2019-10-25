import splitFile

#filename = input('Filepath with single quotations e.g \'filepath.csv\':)
filename = '/Users/blairjackson/Downloads/test.csv'

columns = splitFile.readCSV(filename)

splitFile.writeCSV(columns)
