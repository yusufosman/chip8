from typing import List

import config
from opcode_decoder import Opcode


class Chip8:
    def __init__(self):
        self.draw_flag: bool = False
        self.memory: List[int] = [0] * 4096
        self.pc: int = config.PC_START
        self.opcode: int = 0
        self.i: int = 0
        self.stack: List = []
        self.v: List[int] = [0] * 16

    def load_rom(self, name):
        print(f'Loading {name}...')
        data = open("roms/" + name + ".rom", "rb").read()
        for i, chunk in enumerate(data):
            self.memory[config.ROM_LOAD_START + i] = chunk
        print('Load finished!')

    def emulate_cycle(self):
        opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        Opcode.execute_opcode(self, opcode)
        # TODO: update timers

    def draw_graphics(self):
        pass

    def set_keys(self):
        pass
