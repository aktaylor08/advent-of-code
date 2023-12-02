#!/usr/bin/env python


class Monkey:
    def __init__(
        self,
        items: list[int],
        operation,
        test: int,
        to_monkey: tuple[int, int],
    ):
        self.items = items
        self.op = operation
        self.test = test
        self.to_monkey = to_monkey
        self.inspected = 0

    def proces_item(self, item: int) -> tuple[int, int]:
        # Process the item and return
        self.inspected += 1
        value = self.op(item)
        if value % self.test == 0:
            return value, self.to_monkey[0]
        else:
            return value, self.to_monkey[1]

    def do_turn(self):
        ret = [self.proces_item(x) for x in self.items]
        self.items = []
        return ret


def main():
    monkeys = [
        Monkey([79, 98], lambda x: x * 19, 23, (2, 3)),
        Monkey([54, 65, 75, 74], lambda x: x + 6, 19, (2, 0)),
        Monkey([79, 60, 97], lambda x: x * x, 13, (1, 3)),
        Monkey([74], lambda x: x + 3, 17, (0, 1)),
    ]
    monkeys = [
        Monkey([77, 69, 76, 77, 50, 58], lambda x: x * 11, 5, (1, 5)),
        Monkey([75, 70, 82, 83, 96, 64, 62], lambda x: x + 8, 17, (5, 6)),
        Monkey([53], lambda x: x * 3, 2, (0, 7)),
        Monkey([85, 64, 93, 64, 99], lambda x: x + 4, 7, (7, 2)),
        Monkey([61, 92, 71], lambda x: x * x, 3, (2, 3)),
        Monkey([79, 73, 50, 90], lambda x: x + 2, 11, (4, 6)),
        Monkey([50, 89], lambda x: x + 3, 13, (4, 3)),
        Monkey([83, 56, 64, 58, 93, 91, 56, 65], lambda x: x + 5, 19, (1, 0)),
    ]
    val = 1
    for x in monkeys:
        val = val * x.test
    for _ in range(10_000):
        for x in monkeys:
            to_move = x.do_turn()
            for value, monkey in to_move:
                new_v = value % val
                monkeys[monkey].items.append(new_v)
    val = sorted([m.inspected for m in monkeys])
    print(val[-1] * val[-2])


if __name__ == "__main__":
    main()
