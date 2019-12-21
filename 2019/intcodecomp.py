#!/usr/bin/python
from operator import add, mul


class IntcodeComp(object):

    def __init__(self, inputs, intcodes):
        self.inputs = inputs or []
        self.mem = intcodes[:]  # copy

        self.op = {
            1: self.add,
            2: self.mul,
            3: self.write,
            4: self.read,
            5: self.jump_true,
            6: self.jump_false,
            7: self.lt,
            8: self.eq
        }

        self.ptr = 0
        self.opcode = 0
        self.modes = [0, 0, 0]

    def _get_params(self, n):
        params = []
        for i in range(0, n):
            addr = self.ptr + i + 1
            param = self._parse_param(self.mem[addr], self.modes[i])
            params.append(param)
        return params

    def _parse_param(self, v, mode):
        return self.mem[v] if not mode else v

    def _jmp(self, func):
        params = self._get_params(2)

        if func(params[0]):
            self.ptr = params[1]
        else:
            self.ptr += 3

    def add(self):
        params = self._get_params(2)
        addr = self.mem[self.ptr + 3]
        self.mem[addr] = add(*params[:2])
        self.ptr += 4

    def mul(self):
        params = self._get_params(2)
        addr = self.mem[self.ptr + 3]
        self.mem[addr] = mul(*params[:2])
        self.ptr += 4

    def write(self):
        if len(self.inputs) == 0:
            return False
        addr = self.mem[self.ptr + 1]
        self.mem[addr] = self.inputs.pop(0)
        self.ptr += 2

    def read(self):
        addr = self.ptr + 1
        value = self._parse_param(self.mem[addr], self.modes[0])
        self.ptr += 2
        return value

    def jump_true(self):
        self._jmp(lambda n: n != 0)

    def jump_false(self):
        self._jmp(lambda n: n == 0)

    def lt(self):
        params = self._get_params(2)
        addr = self.mem[self.ptr + 3]
        self.mem[addr] = int(params[0] < params[1])
        self.ptr += 4

    def eq(self):
        params = self._get_params(2)
        addr = self.mem[self.ptr + 3]
        self.mem[addr] = int(params[0] == params[1])
        self.ptr += 4

    def _parse_instruction(self):
        inst = "{:05}".format(self.mem[self.ptr])
        self.opcode = int(inst[3:5])
        self.modes[0] = int(inst[2])
        self.modes[1] = int(inst[1])
        self.modes[2] = int(inst[0])

    def run(self, inp=[]):
        self.inputs.extend(inp)
        while True:
            self._parse_instruction()

            if self.opcode == 99:
                return True

            res = self.op[self.opcode]()
            if res is False:  # when write has no inputs
                break
            if isinstance(res, int):
                return res

            if self.ptr >= len(self.mem):
                break

tests = [
    {
        "mem": [3,9,8,9,10,9,4,9,99,-1,8],  # inp eq 8 position mode
        "inp": [8],
        "res": 1
    },
    {
        "mem": [3,9,8,9,10,9,4,9,99,-1,8],  # inp eq 8 position mode
        "inp": [7],
        "res": 0
    },
    {
        "mem": [3,9,8,9,10,9,4,9,99,-1,8],  # inp eq 8 position mode
        "inp": [9],
        "res": 0
    },
    {
        "mem": [3,9,7,9,10,9,4,9,99,-1,8],  # inp lt 8 position mode
        "inp": [9],
        "res": 0
    },
    {
        "mem": [3,9,7,9,10,9,4,9,99,-1,8],  # inp lt 8 position mode
        "inp": [8],
        "res": 0
    },
    {
        "mem": [3,9,7,9,10,9,4,9,99,-1,8],  # inp lt 8 position mode
        "inp": [7],
        "res": 1
    },
    {
        "mem": [3,3,1108,-1,8,3,4,3,99],    # inp eq 8 immediate mode
        "inp": [9],
        "res": 0
    },
    {
        "mem": [3,3,1108,-1,8,3,4,3,99],    # inp eq 8 immediate mode
        "inp": [8],
        "res": 1
    },
    {
        "mem": [3,3,1108,-1,8,3,4,3,99],    # inp eq 8 immediate mode
        "inp": [7],
        "res": 0
    },
    {
        "mem": [3,3,1107,-1,8,3,4,3,99],    # lt 8 immediate mode
        "inp": [9],
        "res": 0
    },
    {
        "mem": [3,3,1107,-1,8,3,4,3,99],    # lt 8 immediate mode
        "inp": [8],
        "res": 0
    },
    {
        "mem": [3,3,1107,-1,8,3,4,3,99],    # lt 8 immediate mode
        "inp": [7],
        "res": 1
    }
]

if __name__ == '__main__':
    for test in tests:
        res = IntcodeComp(test["inp"], test["mem"]).run()
        if not(res == test["res"]):
            print("Program %s failed with output: %s, expected: %s" % (test["mem"], res, test["res"]))
