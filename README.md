This repository contains test scripts for CoE 111 lab.

# MP: UART

The following scripts can be used to verify the functionality of your design. It uses a serial interface through a USB device. All scripts should be run using Python 3. This can be invoked in the lab workstations using the python3.6 command.

## Test 1: Listen for UART transmissions

Test 1 loops serial reads from the USB serial terminal. The script is `uart_listen.py`. Invoke the script using a terminal:

`snap@exia:$ python3.6 uart_listen.py`

The script has three optional parameters:

- `-d DEVICE` : Specifies the USB serial device interface. By default this is set to `/dev/ttyUSB0`

- `-t TIMEOUT` : Specifies serial read timeout. Set to 2 secs by default

- `-b BAUDRATE` : Specifies the UART baud rate. Set to 9600 by default

Use this script to verify the base specs (sec 2.2) and milestone 3.1.

To end the script, just press Ctrl-c

## Test 2: Transmit 1 byte, Receive 1 byte

Test 2 loops a transmit then listen routine. The bytes transmitted are specified by an external text file. The script is `uart_echo.py`. Invoke the script using a terminal:

`snap@exia:$ python3.6 uart_echo.py`

The script has four optional parameters:

- `-d DEVICE` : Specifies the USB serial device interface. By default this is set to `/dev/ttyUSB0`

- `-t TIMEOUT` : Specifies serial read timeout. Set to 2 secs by default

- `-b BAUDRATE` : Specifies the UART baud rate. Set to 9600 by default

- `-f FILETEST` : Specifies the text file that contains the bytes to be transmitted. By default, this is set to `uart_echo.txt`. Refer to the contents of the said file for the correct format

Use this script to verify extended milestone 3.2.

To end the script, just press Ctrl-c

## Test 3: Transmit byte stream, Receive byte stream

Test 3 is essentially the same as Test 2, except that all bytes in the text file are sent first before listening for transmissions from the FPGA. The script is `uart_multecho.py`. Invocation and options are similar to Test 2.

Use this script to verify extended milestone 3.3.

To end the script, just press Ctrl-c
