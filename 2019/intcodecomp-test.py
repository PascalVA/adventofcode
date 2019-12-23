#!/usr/bin/env python3

from unittest import TestCase, main
from intcodecomp import IntcodeComp

class TestIntcodeComp(TestCase):

    def test_exit(self):
        out = IntcodeComp(
                [],
                [99]
        ).run()
        self.assertTrue(out)

    def test_add(self):
        out = IntcodeComp([], [1, 7, 8, 9, 4, 9, 99, 2, 4, 0]).run()
        self.assertEqual(out, 6)
        out = IntcodeComp([], [1101, 4, 5, 7, 4, 7, 99, 0]).run()
        self.assertEqual(out, 9)
        # rb + 3 (immediate)
        # add 4+5 (immediate)
        # save to 6 + 3 (rb) -> 9
        # return position 9
        out = IntcodeComp([], [109, 3, 21101, 4, 5, 6, 4, 9, 99, 0]).run()
        self.assertEqual(out, 9)

    def test_mul(self):
        out = IntcodeComp([], [2, 7, 8, 9, 4, 9, 99, 2, 4, 0]).run()
        self.assertEqual(out, 8)
        out = IntcodeComp([], [1102, 4, 5, 7, 4, 7, 99, 0]).run()
        self.assertEqual(out, 20)
        # rb + 3 (immediate)
        # add 4*5 (immediate)
        # save to 6 + 3 (rb) -> 9
        # return position 9
        out = IntcodeComp([], [109, 3, 21102, 4, 5, 6, 4, 9, 99, 0]).run()
        self.assertEqual(out, 20)

    def test_read_write(self):
        out = IntcodeComp([4], [3, 5, 4, 5, 99, 0]).run()
        self.assertEqual(out, 4)
        # with rb
        out = IntcodeComp([4], [109, 2, 203, 5, 204, 5, 99, 0]).run()
        self.assertEqual(out, 4)

    def test_jump_true(self):
        #                      0  1  2   3    4  5   6  7  8
        out = IntcodeComp([], [5, 7, 8, 99, 104, 1, 99, 1, 4]).run()
        self.assertEqual(out, 1)
        #                      0    1    2  3  4   5    6   7  8   9 10
        out = IntcodeComp([], [109, 2, 2205, 7, 8, 99, 104, 1, 99, 1, 4]).run()
        self.assertEqual(out, 1)

    def test_jump_false(self):
        #                      0  1  2   3    4  5   6  7  8
        out = IntcodeComp([], [5, 7, 8, 99, 104, 1, 99, 1, 4]).run()
        self.assertEqual(out, 1)
        #                      0    1    2  3  4   5    6   7  8   9 10
        out = IntcodeComp([], [109, 2, 2205, 7, 8, 99, 104, 1, 99, 0, 4]).run()
        self.assertEqual(out, 1)

    def test_lt(self):
        #                      0  1  2  3  4  5   6  7  8  9
        out = IntcodeComp([], [7, 7, 8, 9, 4, 9, 99, 1, 2, 0]).run()
        self.assertEqual(out, 1)
        #                      0    1      2  3  4  5    6  7  8  9 10 11
        out = IntcodeComp([], [109, 2, 22207, 7, 8, 9, 204, 9, 99, 1, 2, 0]).run()
        self.assertEqual(out, 1)

    def test_eq(self):
        #                      0  1  2  3  4  5   6  7  8  9
        out = IntcodeComp([], [8, 7, 8, 9, 4, 9, 99, 1, 1, 0]).run()
        self.assertEqual(out, 1)
        #                      0    1      2  3  4  5    6  7  8  9 10 11
        out = IntcodeComp([], [109, 2, 22208, 7, 8, 9, 204, 9, 99, 1, 1, 0]).run()
        self.assertEqual(out, 1)

    def test_rb_offset(self):
        #                      0  1      2  3  4  5    6  7   8  9 10 11 12
        out = IntcodeComp([], [9, 12, 22208, 7, 8, 9, 204, 9, 99, 1, 1, 0, 2]).run()
        self.assertEqual(out, 1)
        #                      0    1      2  3  4  5    6  7   8  9 10 11
        out = IntcodeComp([], [109, 2, 22208, 7, 8, 9, 204, 9, 99, 1, 1, 0]).run()
        self.assertEqual(out, 1)

    def test_examplse(self):
        # inp eq 8 position mode
        out = IntcodeComp([8], [3,9,8,9,10,9,4,9,99,-1,8]).run()
        self.assertEqual(out, 1)
        # inp lt 8 position mode
        out = IntcodeComp([7], [3,9,7,9,10,9,4,9,99,-1,8]).run()
        self.assertEqual(out, 1)
        # inp lt 8 position mode
        out = IntcodeComp([7], [3,9,7,9,10,9,4,9,99,-1,8]).run()
        self.assertEqual(out, 1)
        # inp eq 8 immediate mode
        out = IntcodeComp([9], [3,3,1108,-1,8,3,4,3,99]).run()
        self.assertEqual(out, 0)
        # lt 8 immediate mode
        out = IntcodeComp([9], [3,3,1107,-1,8,3,4,3,99]).run()
        self.assertEqual(out, 0)
        # produce self as output
        out = run_program([], [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
        self.assertEqual(out, [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
        # return 16 digit number
        out = IntcodeComp([], [1102,34915192,34915192,7,4,7,99,0]).run()
        self.assertEqual(len(str(out).strip()), 16)
        # return large number in the middle
        out = IntcodeComp([], [104,1125899906842624,99]).run()
        self.assertEqual(out, 1125899906842624)


def run_program(inputs, prog):
        outputs = []
        comp = IntcodeComp(inputs, prog)
        while True:
            out = comp.run()
            if out is True:
                break
            outputs.append(out)
        return outputs


if __name__ == "__main__":
    main()
