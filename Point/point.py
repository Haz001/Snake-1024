class Point:
    """
    A 2 Dimensional Coordinate Type

    :attr:
        x - X Coordinate
        y - Y Coordinate
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def as_tuple(self):
        return (
            self.x,
            self.y,
        )

    @property
    def as_list(self):
        return [
            self.x,
            self.y,
        ]

    def __str__(self):
        return f'{self.as_tuple}'

    def __repr__(self):
        class_name = self.__class__.__name__
        # formatted string, !r - shorthand for repr
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __iter__(self) -> iter:
        """
        :return: iterive of x, y
        """
        return iter(self.as_tuple)

    def __eq__(self, other):
        tother: str = type(other).__name__
        result: bool
        match tother:
            case str(self.__class__.__name__):
                result = (self.x == other.x) and (self.y == other.y)
            case 'tuple':
                result = self.as_tuple == other
            case 'list':
                result = self.as_list == other
            case _:
                print(f"Can't compare {tother} to {self.__class__}")
                result = False
        return result

    def __getitem__(self, key):
        if isinstance(key, int):
            try:
                self.as_tuple[key]
            except IndexError as e:
                print(e)
                raise IndexError(
                    f'{self.__class__.__name__} index out of range'
                )

    def __round__(self, n):
        x = self.x.__round__(n)
        y = self.y.__round__(n)
        return self.__init__(x, y)

    def __floor__(self):
        x = self.x.__floor__()
        y = self.y.__floor__()
        return self.__init__(x, y)

    def __ceil__(self):
        x = self.x.__ceil__()
        y = self.y.__ceil__()
        return self.__init__(x, y)
