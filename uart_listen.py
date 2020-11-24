import argparse
import serial

# Parse arguments
parser = argparse.ArgumentParser()

parser.add_argument("-d", "--device", help="USB device (/dev/ttyUSBx)")
#parser.add_argument("-f", "--filetest", help="File containing test cases")
parser.add_argument("-t", "--timeout", help="Timeout for serial read")
parser.add_argument("-b", "--baudrate", help="Baud rate")
args = parser.parse_args()

if args.device:
  dev = args.device
else:
  dev = '/dev/ttyUSB0'

#if args.filetest:
#  test = args.filetest
#else:
#  test = 'uart_echo.txt'

if args.timeout:
  timeout = float(args.timeout)
else:
  timeout = 2.0 

if args.baudrate:
  baud = int(args.baudrate)
else:
  baud = 9600

print('UART echo test')
print('- device: {}'.format(dev))
#print('- test inputs: {}'.format(test))
print('- timeout: {}s'.format(timeout))

try:
  ser = serial.Serial(port=dev, baudrate=baud, timeout=timeout)

except:
  print('Cannot find serial device')
  quit()

#try:
#  f = open(test,'r')
#except:
#  print('Error opening test input file')
#  quit()

#for line in f:
#  data_byte = (int(line,16)).to_bytes(1,'big')
#  print('Transmit to FPGA: {}'.format(hex(int.from_bytes(data_byte,'big'))))
#  ser.write(data_byte)
while 1:
  rxbyte = ser.read()
  print('Received from FPGA: {}'.format(hex(int.from_bytes(rxbyte,'big'))))
  print('')

