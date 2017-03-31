from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

modules = SchLib(tool=SKIDL).add_parts(*[
        Part(name='Arduino_Nano_v3.x',dest=TEMPLATE,tool=SKIDL,keywords='Arduino nano microcontroller module USB',description='Arduino Nano v3.x',ref_prefix='A',num_units=1,fplist=['Arduino*Nano*'],do_erc=True,aliases=['Arduino_Nano_v2.x'],pins=[
            Pin(num='1',name='D1/TX',func=Pin.BIDIR,do_erc=True),
            Pin(num='2',name='D0/RX',func=Pin.BIDIR,do_erc=True),
            Pin(num='3',name='RESET',do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='D2',func=Pin.BIDIR,do_erc=True),
            Pin(num='6',name='D3',func=Pin.BIDIR,do_erc=True),
            Pin(num='7',name='D4',func=Pin.BIDIR,do_erc=True),
            Pin(num='8',name='D5',func=Pin.BIDIR,do_erc=True),
            Pin(num='9',name='D6',func=Pin.BIDIR,do_erc=True),
            Pin(num='10',name='D7',func=Pin.BIDIR,do_erc=True),
            Pin(num='20',name='A1',func=Pin.BIDIR,do_erc=True),
            Pin(num='30',name='VIN',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='D8',func=Pin.BIDIR,do_erc=True),
            Pin(num='21',name='A2',func=Pin.BIDIR,do_erc=True),
            Pin(num='12',name='D9',func=Pin.BIDIR,do_erc=True),
            Pin(num='22',name='A3',func=Pin.BIDIR,do_erc=True),
            Pin(num='13',name='D10',func=Pin.BIDIR,do_erc=True),
            Pin(num='23',name='A4',func=Pin.BIDIR,do_erc=True),
            Pin(num='14',name='D11',func=Pin.BIDIR,do_erc=True),
            Pin(num='24',name='A5',func=Pin.BIDIR,do_erc=True),
            Pin(num='15',name='D12',func=Pin.BIDIR,do_erc=True),
            Pin(num='25',name='A6',func=Pin.BIDIR,do_erc=True),
            Pin(num='16',name='D13',func=Pin.BIDIR,do_erc=True),
            Pin(num='26',name='A7',func=Pin.BIDIR,do_erc=True),
            Pin(num='17',name='3V3',func=Pin.PWROUT,do_erc=True),
            Pin(num='27',name='+5V',func=Pin.PWROUT,do_erc=True),
            Pin(num='18',name='AREF',func=Pin.PWRIN,do_erc=True),
            Pin(num='28',name='RESET',do_erc=True),
            Pin(num='19',name='A0',func=Pin.BIDIR,do_erc=True),
            Pin(num='29',name='GND',func=Pin.PWRIN,do_erc=True)]),
        Part(name='NUCLEO64-FR411RE',dest=TEMPLATE,tool=SKIDL,keywords='STM32 Nucleo ST',description='Nucleo 64 Development Board with STM32F411RET6 MCU, 128kB RAM, 512KB FLASH',ref_prefix='U',num_units=1,fplist=['ST?Morpho?Connector?64?With?STLink*'],do_erc=True,pins=[
            Pin(num='1',name='PC10',func=Pin.BIDIR,do_erc=True),
            Pin(num='2',name='PC11',func=Pin.BIDIR,do_erc=True),
            Pin(num='3',name='PC12',func=Pin.BIDIR,do_erc=True),
            Pin(num='4',name='PD2',func=Pin.BIDIR,do_erc=True),
            Pin(num='5',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='E5V',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='~BOOT0',do_erc=True),
            Pin(num='8',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='10',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='20',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='30',name='PA1',func=Pin.BIDIR,do_erc=True),
            Pin(num='40',name='PC8',func=Pin.BIDIR,do_erc=True),
            Pin(num='50',name='PA12',func=Pin.BIDIR,do_erc=True),
            Pin(num='60',name='PB2',func=Pin.BIDIR,do_erc=True),
            Pin(num='70',name='AGND',func=Pin.PWRIN,do_erc=True),
            Pin(num='80',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='21',name='PB7',func=Pin.BIDIR,do_erc=True),
            Pin(num='31',name='PH1',func=Pin.BIDIR,do_erc=True),
            Pin(num='41',name='PB8',func=Pin.BIDIR,do_erc=True),
            Pin(num='51',name='PA6',func=Pin.BIDIR,do_erc=True),
            Pin(num='61',name='PA8',func=Pin.BIDIR,do_erc=True),
            Pin(num='71',name='PA10',func=Pin.BIDIR,do_erc=True),
            Pin(num='12',name='IOREF',func=Pin.PWRIN,do_erc=True),
            Pin(num='22',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='32',name='PA4',func=Pin.BIDIR,do_erc=True),
            Pin(num='42',name='PC6',func=Pin.BIDIR,do_erc=True),
            Pin(num='52',name='PA11',func=Pin.BIDIR,do_erc=True),
            Pin(num='62',name='PB1',func=Pin.BIDIR,do_erc=True),
            Pin(num='72',name='PC4',func=Pin.BIDIR,do_erc=True),
            Pin(num='13',name='STLINK_TMS/PA13',func=Pin.BIDIR,do_erc=True),
            Pin(num='23',name='PC13',func=Pin.BIDIR,do_erc=True),
            Pin(num='33',name='VBAT',func=Pin.PWRIN,do_erc=True),
            Pin(num='43',name='PB9',func=Pin.BIDIR,do_erc=True),
            Pin(num='53',name='PA7',func=Pin.BIDIR,do_erc=True),
            Pin(num='63',name='PB10',func=Pin.BIDIR,do_erc=True),
            Pin(num='73',name='STLINK_UART_TX/PA2',func=Pin.BIDIR,do_erc=True),
            Pin(num='14',name='~RESET',do_erc=True),
            Pin(num='24',name='VIN',func=Pin.PWRIN,do_erc=True),
            Pin(num='34',name='PB0',func=Pin.BIDIR,do_erc=True),
            Pin(num='44',name='PC5',func=Pin.BIDIR,do_erc=True),
            Pin(num='54',name='PB12',func=Pin.BIDIR,do_erc=True),
            Pin(num='64',name='PB15',func=Pin.BIDIR,do_erc=True),
            Pin(num='74',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='15',name='STLINK_TCK/PA14',func=Pin.BIDIR,do_erc=True),
            Pin(num='25',name='PC14',func=Pin.BIDIR,do_erc=True),
            Pin(num='35',name='PC2',func=Pin.BIDIR,do_erc=True),
            Pin(num='45',name='AVDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='55',name='PB6',func=Pin.BIDIR,do_erc=True),
            Pin(num='65',name='PB4',func=Pin.BIDIR,do_erc=True),
            Pin(num='75',name='STLINK_UART_RX/PA3',func=Pin.BIDIR,do_erc=True),
            Pin(num='16',name='+3V3',func=Pin.PWRIN,do_erc=True),
            Pin(num='26',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='36',name='PC1',func=Pin.BIDIR,do_erc=True),
            Pin(num='46',name='U5V',func=Pin.PWRIN,do_erc=True),
            Pin(num='56',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='66',name='PB14',func=Pin.BIDIR,do_erc=True),
            Pin(num='76',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='17',name='PA15',func=Pin.BIDIR,do_erc=True),
            Pin(num='27',name='PC15',func=Pin.BIDIR,do_erc=True),
            Pin(num='37',name='PC3',func=Pin.BIDIR,do_erc=True),
            Pin(num='47',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='57',name='PC7',func=Pin.BIDIR,do_erc=True),
            Pin(num='67',name='PB5',func=Pin.BIDIR,do_erc=True),
            Pin(num='77',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='18',name='+5V',func=Pin.PWRIN,do_erc=True),
            Pin(num='28',name='PA0',func=Pin.BIDIR,do_erc=True),
            Pin(num='38',name='PC0',func=Pin.BIDIR,do_erc=True),
            Pin(num='48',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='58',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='68',name='PB13',func=Pin.BIDIR,do_erc=True),
            Pin(num='78',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='19',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='29',name='PH0',func=Pin.BIDIR,do_erc=True),
            Pin(num='39',name='PC9',func=Pin.BIDIR,do_erc=True),
            Pin(num='49',name='PA5',func=Pin.BIDIR,do_erc=True),
            Pin(num='59',name='PA9',func=Pin.BIDIR,do_erc=True),
            Pin(num='69',name='STLINK_SWO/PB3',func=Pin.BIDIR,do_erc=True),
            Pin(num='79',name='GND',func=Pin.PWRIN,do_erc=True)]),
        Part(name='Pololu_Breakout_A4988',dest=TEMPLATE,tool=SKIDL,keywords='Pololu Breakout Board Stepper Driver A4988',description='Pololu Breakout Board, Stepper Driver A4988',ref_prefix='A',num_units=1,fplist=['Pololu*Breakout*15.2x20.3mm*'],do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='1B',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='1A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='2A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='2B',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='VMOT',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='~ENABLE',do_erc=True),
            Pin(num='10',name='MS1',do_erc=True),
            Pin(num='11',name='MS2',do_erc=True),
            Pin(num='12',name='MS3',do_erc=True),
            Pin(num='13',name='~RESET',do_erc=True),
            Pin(num='14',name='~SLEEP',do_erc=True),
            Pin(num='15',name='STEP',do_erc=True),
            Pin(num='16',name='DIR',do_erc=True)]),
        Part(name='Pololu_Breakout_DRV8825',dest=TEMPLATE,tool=SKIDL,keywords='Pololu Breakout Board Stepper Driver DRV8825',description='Pololu Breakout Board, Stepper Driver DRV8825',ref_prefix='A',num_units=1,fplist=['Pololu*Breakout*15.2x20.3mm*'],do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='~FLT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='B2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='B1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='A1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='A2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='VMOT',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='~EN',do_erc=True),
            Pin(num='10',name='M0',do_erc=True),
            Pin(num='11',name='M1',do_erc=True),
            Pin(num='12',name='M2',do_erc=True),
            Pin(num='13',name='~RST',do_erc=True),
            Pin(num='14',name='~SLP',do_erc=True),
            Pin(num='15',name='STEP',do_erc=True),
            Pin(num='16',name='DIR',do_erc=True)])])