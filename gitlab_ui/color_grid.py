from npyscreen import GridColTitles


class ColorGrid(GridColTitles):

    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value == 'FAIL':
            actual_cell.color = 'DANGER'
        elif cell_display_value == 'PASS':
            actual_cell.color = 'GOOD'
        else:
            actual_cell.color = 'DEFAULT'
