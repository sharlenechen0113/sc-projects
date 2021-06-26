"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

FILE: Breakout Graphics
NAME: Sharlene Chen
--------------------------------
TODO:
Creates a breakout game -- the ball will bounce on the paddle and the bricks will disappear
if hit by the ball. The game has a total of 3 lives, when the player fails to catch the ball by
the paddle before hitting all bricks, the player loses. Once the player successfully removes all bricks
within 3 lives the player wins.
"""
from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    while True:
        global NUM_LIVES
        graphics.check_collision()
        graphics.remove_brick()
        if graphics.double_score_exist is True:
            graphics.double_score.move(0, 7)
            graphics.double_score_switch()
            if graphics.double_score_start is True:
                graphics.double_score_exec()
        if graphics.shorten_paddle_exist is True:
            graphics.shorten_paddle.move(0, 7)
            graphics.shorten_paddle_switch()
            if graphics.shorten_paddle_start is True:
                graphics.shorten_paddle_exec()
        if graphics.no_bricks():
            graphics.win_game()
            break
        if graphics.ball.x <= 0 or (graphics.ball.x + graphics.ball.width) > graphics.window.width:
            graphics.set_velocity_x()
        elif graphics.ball.y <= 0:
            graphics.set_velocity_y()
        dx = graphics.get_velocity_x()
        dy = graphics.get_velocity_y()
        graphics.ball.move(dx, dy)
        graphics.update_score()
        if graphics.ball.y > graphics.window.height:
            NUM_LIVES -= 1
            if NUM_LIVES == 2:
                graphics.window.remove(graphics.heart3)
                graphics.reset_ball()
            elif NUM_LIVES == 1:
                graphics.window.remove(graphics.heart2)
                graphics.reset_ball()
            elif NUM_LIVES <= 0:
                graphics.window.remove(graphics.heart1)
                graphics.game_over()
                break
        pause(FRAME_RATE)




if __name__ == '__main__':
    main()
