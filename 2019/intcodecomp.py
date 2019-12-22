#!/usr/bin/python
from operator import add, mul
from array import array


class IntcodeMem(object):

    def __init__(self, memory):
        self.mem = {}
        for i, item in enumerate(memory):
            self.mem[i] = item

    def __getitem__(self, index):
        return self.mem.get(index, 0)

    def __setitem__(self, index, value):
        self.mem[index] = value


class IntcodeComp(object):

    def __init__(self, inputs, program):
        self.inputs = inputs or []

        self.mem = IntcodeMem(program)

        self.op = {
            1: self.add,
            2: self.mul,
            3: self.write,
            4: self.read,
            5: self.jump_true,
            6: self.jump_false,
            7: self.lt,
            8: self.eq,
            9: self.rb_offset
        }

        self.ptr = 0
        self.rb = 0  # relative base
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
        return {
          0: self.mem[v],           # position mode
          1: v,                     # immediate mode
          2: self.mem[v + self.rb]  # relative mode
        }[mode]

    def _parse_write_param(self, v, mode):
        if mode == 1:
            raise ValueError("Write params can never have immediate mode (1)")
        return {
          0: self.mem[v],           # position mode
          2: self.mem[v] + self.rb  # relative mode
        }[mode]

    def _jmp(self, func):
        params = self._get_params(2)

        if func(params[0]):
            self.ptr = params[1]
        else:
            self.ptr += 3

    def add(self):
        params = self._get_params(2)
        addr = self._parse_write_param(self.ptr + 3, self.modes[2])
        self.mem[addr] = add(*params[:2])
        self.ptr += 4

    def mul(self):
        params = self._get_params(2)
        addr = self._parse_write_param(self.ptr + 3, self.modes[2])
        self.mem[addr] = mul(*params[:2])
        self.ptr += 4

    def write(self):
        if len(self.inputs) == 0:
            return False
        addr = self._parse_write_param(self.ptr + 1, self.modes[0])
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
        addr = self._parse_write_param(self.ptr + 3, self.modes[2])
        self.mem[addr] = int(params[0] < params[1])
        self.ptr += 4

    def eq(self):
        params = self._get_params(2)
        addr = self._parse_write_param(self.ptr + 3, self.modes[2])
        self.mem[addr] = int(params[0] == params[1])
        self.ptr += 4

    def rb_offset(self):
        self.rb += self._parse_param(self.mem[self.ptr + 1], self.modes[0])
        self.ptr += 2

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

            #print("mem: %s\nptr: %d, op: %d, modes: %s, rb: %s"
            #       % (self.mem.mem.values(), self.ptr, self.opcode, self.modes, self.rb))
            #from time import sleep
            #sleep(0.5)

            if self.opcode == 99:
                self.ptr = 0
                return True

            res = self.op[self.opcode]()
            if res is False:  # when write has no inputs
                break
            if isinstance(res, int):
                return res
