from selene.core.entity import Element


class Table:

    def __init__(self, element: Element):
        self.element = element

    def path_to_cell(self, row: int, column: int):
        return self.element.all('tbody tr')[row - 1].all('td')[column - 1]