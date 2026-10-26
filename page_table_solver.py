"""
Author: TJ Drape

Date Started: October 21, 2026
Date Finished: 

Purpose: 
Model the ways an OS uses page tables, memory frames, and more to efficiently store data
in a non-contiguous memory format.

Assumptions:
In this model, I am assuming that MemoryModel is only created and ran once. I have only tested it for that.
Also, I am assuming that the given displacement is valid, since all rows in the example give a valid displacement. 

Sources of Help: Claude

AI-Guided Decisions:
Give an Assumptions clause.
Verify output.
PTLR checked using > instead of >=.
PTLR didn't check if the frame was negative.

"""

# We are given a scenario with 19 rows and the following columns
# Row Num
# Process
# Page
# Displacement

# We have to map the process into RAM memory
# If the page doesn't exist for a page table, print an error message and continue

# Need to model how RAM is configured

# We have f0 through f12, which models RAM cells 0 through 25 (each cell has 1 displacement as well)

# PT1 => P0: f7, P1: f12, P2: f4
# PT2 => P0: f9, P1: f11, P2: f1, P3: f3, P4: f6, P5: f0
# PT3 => P0: f5, P1: f10, P2: f8, P3: f2

class MemoryCell:
    def __init__(self, number):
        self.number = number
        self.filled = False

    def fill(self):
        self.filled = True

# Create 3 page tables
# Map pages to both memory cells, include displacement
# pages_with_link => [page_0_f_value, etc.]

class inputRow:
    def __init__(self, number, process, page, displacement):
        self.number = number
        self.process = process
        self.page = page
        self.displacement = displacement

# all_processes = [<rows of data>]
# all process map to the same page table: p0 = pt0, etc.

class MemoryModel:
    def __init__(self, num_cells, num_displacement, processes):
        self.num_cells = num_cells
        self.num_displacement = num_displacement
        self.processes = processes
        self.memory_cells = self.make_memory_cells(num_cells, num_displacement)
        self.page_tables = [PageTable(3, [7, 12, 4]), PageTable(6, [9, 11, 1, 3, 6, 0]), PageTable(4, [5, 10, 8, 2])]

    def make_memory_cells(self, num_cells, num_displacement):
        memory_cells = []
        for i in range(num_cells):
            for _ in range(num_displacement):
                memory_cells.append(MemoryCell(i))

        return memory_cells

    def map_data_to_memory(self, row: inputRow):
        pt = self.page_tables[row.process - 1]
        if (row.page > (pt.ptlr - 1)) or (row.page < 0):
                    print(f"""
------------------------------------------------------    

Number:         {row.number}
Process:        {row.process}
Page:           {row.page}
Displacement:   {row.displacement}

Running the program to map this value to RAM memory

    ERROR. Page Value Invalid for Page Table

------------------------------------------------------
        """)
                    
        else: 
            memory_frame = pt.memory_locations[row.page]
            memory_cell = (memory_frame * 2) + row.displacement
            print(f"""
------------------------------------------------------    

Number:         {row.number}
Process:        {row.process}
Page:           {row.page}
Displacement:   {row.displacement}

Running the program to map this value to RAM memory

Memory Frame:    f{memory_frame}

Memory Cell:    #{memory_cell}

------------------------------------------------------
            """)
            self.memory_cells[memory_cell].fill()

    def run(self):
        for process in self.processes:
            self.map_data_to_memory(process)

        
            
class PageTable:
    def __init__(self, ptlr, memory_locations):
        self.ptlr = ptlr
        # for each page, since indexed from 0, we can use its position in the list as the page number
        self.memory_locations = memory_locations



# Map the Processes to the Page Table Base Register (PTBR)
# P1 => PT1
# P2 => PT2
# P3 => PT3

# Have to respect the Page Table Length Registers (PTLRs)
# P1: PT1 => 3
# P2: PT2 => 6
# P3: PT3 => 4
# Only the process has this, but using the PT variable makes it easier for me to understand


# Scenario 1:
all_processes = [
inputRow(1, 1, 0, 0),
inputRow(2, 3, 1, 1),
inputRow(3, 2, 5, 0),
inputRow(4, 2, 2, 1),
inputRow(5, 2, 0, 0),
inputRow(6, 1, 0, 1),
inputRow(7, 3, 5, 0),
inputRow(8, 2, 5, 1),
inputRow(9, 2, 3, 0),
inputRow(10, 2, 0, 1),
inputRow(11, 1, 1, 0),
inputRow(12, 3, 2, 1),
inputRow(13, 3, 0, 0),
inputRow(14, 2, 3, 1),
inputRow(15, 2, 1, 0),
inputRow(16, 1, 1, 1),
inputRow(17, 3, 3, 0),
inputRow(18, 3, 0, 1),
inputRow(19, 2, 4, 0),
]

# Scenario 2:
# all_processes = [
# inputRow(1, 3, 2, 0),
# inputRow(2, 2, 5, 1),
# inputRow(3, 2, 3, 0),
# inputRow(4, 2, 0, 1),
# inputRow(5, 1, 4, 0),
# inputRow(6, 3, 2, 1),
# inputRow(7, 3, 0, 0),
# inputRow(8, 2, 3, 1),
# inputRow(9, 2, 1, 0),
# inputRow(10, 1, 1, 1),
# inputRow(11, 3, 3, 0),
# inputRow(12, 3, 0, 1),
# inputRow(13, 2, 4, 0),
# inputRow(14, 2, 1, 1),
# inputRow(15, 1, 2, 0),
# inputRow(16, 3, 3, 1),
# inputRow(17, 3, 1, 0),
# inputRow(18, 2, 4, 1),
# inputRow(19, 2, 2, 0),
# ]

m = MemoryModel(26, 1, all_processes)
m.run()
    
