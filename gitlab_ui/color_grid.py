from npyscreen import SimpleGrid


class ColorGrid(SimpleGrid):

    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value == 'FAIL':
            actual_cell.color = 'DANGER'
            actual_cell.use_max_space = True
        elif cell_display_value == 'PASS':
            actual_cell.color = 'GOOD'
            actual_cell.use_max_space = True
        else:
            actual_cell.color = 'DEFAULT'
            actual_cell.use_max_space = True
