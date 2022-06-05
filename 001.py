import logging
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time
import serial
import pymysql

PORT = '/dev/ttyUSB0'
logger = modbus_tk.utils.create_logger("console")
master = modbus_rtu.RtuMaster(
    serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
)
master.set_timeout(5.0)
master.set_verbose(True)
print('STARTING...')
logger.info("Transducer connected")

conn = pymysql.connect(host='192.168.1.120',port=3306,user='root',password='root',database='equip',charset='utf8mb4')
print("Database connected")
print('STARTING...')

var = 1
while var == 1:
        # 读保持寄存器
        signal = master.execute(1, cst.READ_HOLDING_REGISTERS,1,12)
        a = time.localtime()
        t = (time.strftime("%Y-%m-%d %H:%M:%S", a))
        try:
                print(signal)

                conn = pymysql.connect(
                        host='192.168.1.120',
                        port=3306,
                        user='root',
                        password='root',
                        database='equip',
                        charset='utf8mb4'
                )
                c = conn.cursor()
                sql1 = '''INSERT INTO t_edge_vibration VALUES ('{}','{}','{}','{}');'''
                sql2 = sql1.format(t,signal[0],signal[1],signal[2])
                c.execute(sql2)
                conn.commit()
                conn.close()
                logger.info('Record created successfully')
        except modbus_tk.modbus.ModbusError as exc:
                logger.error("%s- Code=%d", exc, exc.get_exception_code())

        print('=====================================================================>>>')
        time.sleep(2)