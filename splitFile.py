def readCSV(filename):
    columns = []
    with open(filename) as csvFile:
        for x in range (1):
            next(csvFile)
        for line in csvFile:
            #split the columns, keep the required ones
            splitLine = line.split(',')
            source = splitLine[3]
            newsource = changeSource(source)
            splitLine[3] = newsource
            columns.append(splitLine)
    return columns

def changeSource(source):
    if source == 'cpc':
        newsource = 'paysearch'
    elif source == 'paid_search':
        newsource = 'paysearch'
    elif source == '(none)':
        newsource = 'direct'
    elif source == 'organic':
        newsource = 'orgsearch'
    else:
        newsource = 'affiliate'
    return newsource



def writeCSV(columns):
    with open('adjustedDyson.csv', 'w') as csvfile:
        #add headers to file
        #web headers
        headers = ('sessiondatetime','sessionId','userCountry','sourcetype','action_shopHomePageVisit','action_productPageVisit','action_addToCartVisit','action_purchaseVisit\n')

        csvfile.write(','.join(headers))
        for line in columns:
            # convert tuple to string and write each line to the file
            line = ','.join(line)
            csvfile.write(line)