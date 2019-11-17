from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chip8 import Chip8


class Opcode:
    @staticmethod
    def get_x(opcode):
        return (opcode & 0x0F00) >> 8

    @classmethod
    def execute_opcode(cls, chip8: 'Chip8', opcode: int):
        if opcode & 0xF000 == 0x0000:
            chip8.i = opcode & 0x0FFF
            chip8.pc += 2
        elif opcode == 0x00EE:
            chip8.pc = chip8.stack.pop()
        elif opcode == 0x00E0:
            pass
        elif opcode & 0xF000 == 0x1000:
            chip8.pc = opcode & 0x0FFF
        elif opcode & 0xF000 == 0x2000:
            chip8.stack.append(chip8.pc)
        elif opcode & 0xF000 == 0x3000:
            if chip8.v[cls.get_x(opcode)] == opcode & 0x00FF:
                chip8.pc += 4
        elif opcode & 0xF000 == 0x6000:
            chip8.v[cls.get_x(opcode)] = opcode & 0x00FF
            chip8.pc += 2
        elif opcode & 0xF000 == 0xA000:
            chip8.i = opcode & 0x0FFF
            chip8.pc += 2
