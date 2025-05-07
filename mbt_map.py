from cyberpi import mbot2, ultrasonic2, audio
import time


WALL_THRESHOLD = 20 #The distance at which the sensor reacts
CELL_SIZE = 10 #Size of 1 square
MAP_SIZE = 7
START_POS = (MAP_SIZE // 2, MAP_SIZE // 2)
DIRECTION_ORDER = ["front", "right", "back", "left"]


grid = [[0.0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
robot_x, robot_y = START_POS
robot_dir = 0  # 0=front, 1=right, 2=back, 3=left


def print_map():
    for y in range(MAP_SIZE):
        row = ""
        for x in range(MAP_SIZE):
            if x == robot_x and y == robot_y:
                row += "R"
            elif grid[y][x] == 1.0:
                row += "#"
            else:
                row += "."
        print(row)
    audio.play("end")


def scan_walls():
    walls = {}
    for i, dir_name in enumerate(DIRECTION_ORDER):
        try:
            dist = ultrasonic2.get(index=1)
            print(dir_name + ": " + str(dist) + "cm")
        except Exception as e:
            print("error: " + str(e))
            dist = -1
        walls[dir_name] = dist
        time.sleep(0.3)
        if i < 3:
            mbot2.turn(90, 50)
            time.sleep(0.2)
    mbot2.turn(90, 50)
    return walls

def mark_walls_on_map(walls, x, y):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for i, dir_name in enumerate(DIRECTION_ORDER):
        dist = walls[dir_name]
        if dist != -1 and dist < 300:
            steps = int(dist / CELL_SIZE)
            wx = x + dx[i] * steps
            wy = y + dy[i] * steps
            if 0 <= wx < MAP_SIZE and 0 <= wy < MAP_SIZE:
                grid[wy][wx] = 1.0


def front_is_clear():
    try:
        dist = ultrasonic2.get(index=1)
        print("front: " + str(dist) + "cm")
        return dist != -1 and dist >= WALL_THRESHOLD
    except:
        return False


def move_forward():
    global robot_x, robot_y
    mbot2.straight(distance=30, speed=70)
    time.sleep(0.5)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    robot_x += dx[robot_dir]
    robot_y += dy[robot_dir]


def turn_right():
    global robot_dir
    mbot2.turn(90, 50)
    time.sleep(0.3)
    robot_dir = (robot_dir + 1) % 4


#search loop
for step in range(10):
    if front_is_clear():
        robot_dir 
        move_forward()
    else:
        print("search start!")
        walls = scan_walls()
        mark_walls_on_map(walls, robot_x, robot_y)
        print_map()
        turn_right()