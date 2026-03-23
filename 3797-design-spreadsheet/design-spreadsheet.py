class Spreadsheet:

    def __init__(self, rows):
        self.rows = rows
        self.grid = [[0] * 26 for _ in range(rows)]
    
    def setCell(self, cell, value):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.grid[row][col] = value
    
    def resetCell(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.grid[row][col] = 0
    
    def getValue(self, formula):
        # remove '='
        formula = formula[1:]
        
        left, right = formula.split('+')
        
        return self.getVal(left) + self.getVal(right)
    
    def getVal(self, x):
        # if number
        if x[0].isdigit():
            return int(x)
        
        # if cell
        col = ord(x[0]) - ord('A')
        row = int(x[1:]) - 1
        return self.grid[row][col]