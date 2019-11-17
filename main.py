from chip8 import Chip8

emulator = Chip8()
emulator.load_rom('pong')

while True:
    emulator.emulate_cycle()
    if emulator.draw_flag:
        emulator.draw_graphics()
    emulator.set_keys()
