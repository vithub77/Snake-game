import curses

from snake import Snake
from food import Food
from game_over import g_v

SPEED = 400
SPEED_W: int
SPEED_H: int
LEVEL: int


def update_speed(level: int = 1):
    global SPEED_W, SPEED_H, SPEED
    _sp = SPEED - (40 * level)
    if _sp:
        SPEED_W = _sp
        SPEED_H = int(SPEED_W * 1.3)


def update_level(sn_len: int):
    global LEVEL
    LEVEL = int(sn_len ** 0.5)


def main(stdscr):
    global SPEED_W, SPEED_H, LEVEL
    update_speed()
    speed = SPEED_W

    course = (1, 0)
    snake_length = 1

    width, height = curses.COLS, curses.LINES - 1
    snake = Snake(width // 2, height // 2)

    win = stdscr.derwin(height, width, 1, 0)
    box = (0, width - 1, 1, height)
    curses.curs_set(0)
    stdscr.nodelay(True)

    food = Food((width - 2, height - 1))

    update_level(1)

    flag = True
    while flag:
        stdscr.clear()
        win.border(0)

        food.cooking()

        button = stdscr.getch()
        if button == ord('q'):
            return
        # key down
        elif button == 258:
            if course != (0, -1) or snake_length == 1:
                course, speed = (0, 1), SPEED_H
        # key up
        elif button == 259:
            if course != (0, 1) or snake_length == 1:
                course, speed = (0, -1), SPEED_H
        # key left
        elif button == 260:
            if course != (1, 0) or snake_length == 1:
                course, speed = (-1, 0), SPEED_W
        # key right
        elif button == 261:
            if course != (-1, 0) or snake_length == 1:
                course, speed = (1, 0), SPEED_W

        snake.update_coordinates(course)
        head = snake.get_coordinates()

        stdscr.addstr(0, 2, f"SNAKE LENGTH: {snake_length}", curses.A_BOLD)
        stdscr.addstr(0, width // 2, f"LEVEL: {LEVEL}", curses.A_BOLD)
        stdscr.addstr(0, width - 10, f"QUIT: q", curses.A_BOLD)

        if head[0] in (box[0], box[1]) or head[1] in (box[2], box[3]):
            break

        for f in food.get_food():
            if head[0] == f[0] and head[1] == f[1]:
                food.del_food(f)
                snake.add_tail()
            else:
                stdscr.addch(f[1], f[0], '*')

        for snake_link in snake.get_snake():
            xy = snake_link.get_coordinates()
            snake_length = snake_link.id
            if xy == head and snake_length != 1:
                flag = False
                stdscr.addch(xy[1], xy[0], '@')
            else:
                stdscr.addch(xy[1], xy[0], '@' if snake_link.id == 1 else '0')

        update_level(snake_length)
        update_speed(LEVEL)
        if LEVEL % 2 and food.flag == LEVEL:
            food.count += 1
            food.flag += 2
        stdscr.refresh()
        curses.napms(speed)

    # stdscr.addstr(height // 2, (width // 2) - 7, "G A M E  O V E R", curses.A_BOLD)
    y, x = height // 2 - 2, int((width - 45) / 2 - 1)
    for letter in "GAME OVER":
        for line in range(5):
            stdscr.addstr(y + line, x, g_v[letter][line])
        stdscr.refresh()
        curses.napms(100)
        y += 0
        x += 6

    stdscr.refresh()
    curses.napms(3500)


if __name__ == "__main__":
    curses.wrapper(main)
