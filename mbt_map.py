from cyberpi import mbot2,ultrasonic2,table

table.add(1, 1, "front")
table.add(1, 2, ultrasonic2.get(index = 1))
mbot2.turn(92, 50)
table.add(2, 1, "right")
table.add(2, 2, ultrasonic2.get(index = 1))
mbot2.turn(92, 50)
table.add(3, 1, "back")
table.add(3, 2, ultrasonic2.get(index = 1))
mbot2.turn(92, 50)
table.add(4, 1, "left")
table.add(4, 2, ultrasonic2.get(index = 1))
mbot2.turn(92, 50)