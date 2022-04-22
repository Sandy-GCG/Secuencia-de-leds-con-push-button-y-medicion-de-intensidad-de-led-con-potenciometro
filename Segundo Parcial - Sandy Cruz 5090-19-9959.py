import pyfirmata 
import time

DELAY_V = 5
DELAY_A = 1
DELAY_R = 4

pinLedPot = 11
pinPush = 4
pinLedV = 7
pinLedA = 8
pinLedR = 13

PORT = 'COM5'   #Puerto al que se conecta el arduino

board = pyfirmata.Arduino(PORT) #La placa se configura con el "pyFirmata" y su puerto correspondiente

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[pinPush].mode = pyfirmata.INPUT

board.analog[0].enable_reporting()

for x in range(3):
    board.digital[pinLedPot].write(1)
    time.sleep(0.5)
    board.digital[pinLedPot].write(0)
    time.sleep(0.5)

analogPot = board.get_pin('a:0:i')
led = board.get_pin('d:11:p')

while True:
    analog = analogPot.read()
    led.write(analog)

    sw = board.digital[pinPush].read()
    if sw is True:
        board.digital[pinLedV].write(1)
        board.pass_time(DELAY_V)
        board.digital[pinLedV].write(0)
        board.digital[pinLedA].write(1)
        board.pass_time(DELAY_A)
        board.digital[pinLedA].write(0)
        board.digital[pinLedR].write(1)
        board.pass_time(DELAY_R)
        board.digital[pinLedR].write(0)
    else:
        board.digital[pinLedV].write(0)
        board.digital[pinLedA].write(0)
        board.digital[pinLedR].write(0)
    time.sleep(0)