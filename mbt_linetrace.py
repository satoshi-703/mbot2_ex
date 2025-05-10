#01
from cyberpi import mbot2,quad_rgb_sensor,event

@event.is_press("b")
def callback():
    while 1:
        sta = quad_rgb_sensor.get_line_sta("middle",1)
        
        if sta == 0:
            mbot2.backward(50)
        elif sta == 1:
            mbot2.turn_right(50)
        elif sta == 2:
            mbot2.turn_left(50)
        elif sta == 3:
            mbot2.forward(50)

#02
from cyberpi import mbot2,quad_rgb_sensor,event

@event.is_press("b")
def callback():
    while 1:
        sta = quad_rgb_sensor.get_line_sta("all",1)
        
        if sta == 8:
            mbot2.turn_left(50)
        elif sta == 1:
            mbot2.turn_right(50)
        else:
            mbot2.forward(50)

#03
import cyberpi

while 1:
    #L1,R1
    cyberpi.table.add(1,1,"L1,R1")
    cyberpi.table.add(1,2,cyberpi.quad_rgb_sensor.get_line_sta("middle",1))
    
    #L2,L1,R1,R2
    cyberpi.table.add(2,1,"L2～R2")
    cyberpi.table.add(2,2,cyberpi.quad_rgb_sensor.get_line_sta("all",1))

    #偏差
    cyberpi.table.add(3,1,"L2～R2")
    cyberpi.table.add(3,2,cyberpi.quad_rgb_sensor.get_offset_track(1))

#04
from cyberpi import mbot2,quad_rgb_sensor,event

@event.is_press("b")
def callback():
    base_spd = 100  #基準速度
    kp = 0.8        #Kp

    while 1:
        #左タイヤ速度
        left_spd = base_spd - (kp * quad_rgb_sensor.get_offset_track(1))
        
        #右タイヤ速度
        right_spd = - base_spd - (kp * quad_rgb_sensor.get_offset_track(1))

        #左右タイヤを個別に制御        
        mbot2.drive_speed(left_spd, right_spd)