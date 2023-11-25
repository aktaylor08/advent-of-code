#!/usr/bin/env python


class Monkey:
    def __init__(
        self,
        start_items: list[int],
        operation: tuple,
        test: int,
        to_monkey: tuple[int, int],
    ):
        self.start_items = start_items
        self.op = operation
        self.test = test
        self.to_monkey = to_monkey

    def proces_item(self, item: int) -> tuple[int, int]:
        # Process the item and return
        pass
