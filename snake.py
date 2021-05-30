#!/usr/bin/env python3

import os
import keyboard
import threading
import time
import subjects
import render


def control(e):
    if e.event_type == 'down' and (e.name in directions) and e.name != snake.direction:
        # Против обратного движения
        if directions.index(e.name) % 2 != directions.index(snake.old_direction) % 2:
            with lock:
                snake.direction = e.name


if __name__ == '__main__':
    directions = ['right', 'up', 'left', 'down']
    lock = threading.Lock()
    if os.name == 'posix':
        os.system('stty -echo')

    try:
        render.warning()
        time.sleep(3)
        while True:
            with lock:
                print('\033[?25l', end='')
            render.cover()
            render.frame()

            snake = subjects.Snake()
            snake.render()
            food = subjects.Food(snake)
            food.render()
            score = 0
            render.score()

            keyboard.hook(control)
            # ГЕЙМПЛЕЙ
            while True:
                time.sleep(0.15)
                with lock:
                    snake.move()
                if snake.hit():
                    break
                snake.render()
                if snake.head == food:
                    snake.add_cell()
                    food = subjects.Food(snake)
                    food.render()
                    score += 1
                    render.score(score)
                snake.update_direction()
            time.sleep(2)
            render.clear()
            render.game_over(score)
            time.sleep(5)
    except KeyboardInterrupt:
        pass

    print('\033[?25h', end='')
    if os.name == 'posix':
        os.system('stty -echo')
