tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    #zero(0) value list to store(later) max len of each list
    colWidths = [0] * len(tableData)

    #store maxlen of each list
    for i in range(len(tableData)):
        colWidths[i] =  len(max(tableData[i], key=len))

    #formatting the printing stage
    for x in range(len(tableData[0])):
        for y in range(len(colWidths)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print(end='\n')

printTable(tableData)
