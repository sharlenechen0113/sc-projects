"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

FILE: Breakout Graphics
NAME: Sharlene Chen
--------------------------------
TODO:
Creates a breakout game -- the ball will bounce on the paddle and the bricks will disappear
if hit by the ball. The game has a total of 3 lives, when the player fails to catch the ball by
the paddle before hitting all bricks, the player loses. Once the player successfully removes all bricks
within 3 lives the player wins.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
SPEED_UP = 0.01     # Speed up constant
SCORE_MULTIPLE = 1  # Points added for each brick hit


class BreakoutGraphics:
    """Initializes the game"""
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.glitch_count = 1
        self.paddle = GRect(paddle_width,paddle_height,x=(self.window_width-paddle_width)/2,y=self.window_height-paddle_offset)
        self.paddle.color = 'black'
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2,ball_radius*2,x=(self.window_width-ball_radius*2)/2,
                          y=(self.window_height-ball_radius*2)/2)
        self.radius = BALL_RADIUS
        self.ball.color = 'black'
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.__speed_up = SPEED_UP

        # Lives
        self.heart1 = GOval(20, 20)
        self.heart1.filled = True
        self.heart1.color = 'magenta'
        self.heart1.fill_color = 'magenta'
        self.heart2 = GOval(20, 20)
        self.heart2.filled = True
        self.heart2.color = 'magenta'
        self.heart2.fill_color = 'magenta'
        self.heart3 = GOval(20, 20)
        self.heart3.filled = True
        self.heart3.color = 'magenta'
        self.heart3.fill_color = 'magenta'
        self.window.add(self.heart1, x=0,y=self.window.height - self.heart1.height - brick_spacing)
        self.window.add(self.heart2, x=0 + (self.heart2.width + brick_spacing) * 1,
                        y=self.window.height - self.heart2.height - brick_spacing)
        self.window.add(self.heart3, x=0 + (self.heart3.width + brick_spacing) * 2,
                        y=self.window.height - self.heart3.height - brick_spacing)

        # Draw bricks
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        for i in range(0,brick_rows):
            for j in range(0,brick_cols):
                self.brick = GRect(brick_width,brick_height,x=0+(brick_width+brick_spacing)*i,
                                   y=brick_offset+(brick_height+brick_spacing)*j)
                self.brick.filled = True
                if j % 10 == 0 or j % 10 == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif j % 10 == 2 or j % 10 == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j % 10 == 4 or j % 10 == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j % 10 == 6 or j % 10 == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif j % 10 == 8 or j % 10 == 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick)
        self.brick_count = 0
        self.total_bricks = brick_cols*brick_rows

        # Draw labels
        self.score = 0
        self.score_multiple = SCORE_MULTIPLE
        self.score_label = GLabel(f'Score: {self.score}', x=0, y=30)
        self.score_label.font = '-30'
        self.window.add(self.score_label)
        self.start_label = GLabel(f'Click to Start',x=self.window.width/5,y=self.window.height*0.666)
        self.start_label.font = '-50'
        self.window.add(self.start_label)
        self.double_score_label = GLabel(f'Yellow Rect: Doubles Score', x=self.window.width / 5, y=self.window.height * 0.7)
        self.double_score_label.font = '-15'
        self.window.add(self.double_score_label)
        self.shorten_paddle_label = GLabel(f'Blue Rect: Shortens Paddle', x=self.window.width / 5,
                                         y=self.window.height * 0.73)
        self.shorten_paddle_label.font = '-15'
        self.window.add(self.shorten_paddle_label)


        # Dropping objects
        self.objects_length = 20
        self.shorten_paddle = GRect(self.objects_length, self.objects_length)
        self.shorten_paddle.filled = True
        self.shorten_paddle_count = 0
        self.shorten_paddle_exist = False
        self.shorten_paddle_start = False
        self.shorten_paddle.fill_color = 'darkblue'
        self.shorten_paddle.color = 'darkblue'
        self.double_score = GRect(self.objects_length,self.objects_length)
        self.double_score.filled = True
        self.double_score_count = 0
        self.double_score_exist = False
        self.double_score_start = False
        self.double_score.fill_color = 'yellow'
        self.double_score.color = 'yellow'

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.paddle_move)

    def paddle_move(self, event):
        """Controls paddle movement"""
        dx = event.x - (self.paddle.x + self.paddle.width/2)
        if self.paddle.x + dx < 0:
            dx = 0 - self.paddle.x
        elif self.paddle.x + self.paddle.width + dx > self.window.width:
            dx = self.window.width - (self.paddle.x + self.paddle.width)
        self.paddle.move(dx, 0)

    def set_velocity(self):
        """Sets the very first moving velocity"""
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def start_game(self,event):
        """Connected to mouse-click event to start game"""
        if self.__dx == 0 and self.__dy == 0:
            self.set_velocity()
            self.window.remove(self.start_label)
            self.window.remove(self.double_score_label)
            self.window.remove(self.shorten_paddle_label)
        else:
            pass

    def get_velocity_x(self):
        """Returns velocity x"""
        return self.__dx

    def get_velocity_y(self):
        """Returns velocity y"""
        return self.__dy

    def set_velocity_x(self):
        """Changes velocity x when hitting an object"""
        self.__dx *= -1

    def set_velocity_y(self):
        """Changes velocity y when hitting an object, speeds up when hitting an object"""
        self.__dy *= -(1+SPEED_UP)

    def remove_brick(self):
        """Removes brick when hit by ball, and drops random item"""
        maybe_brick = self.window.get_object_at(self.ball.x, self.ball.y)
        if maybe_brick is not None and maybe_brick is not self.double_score and maybe_brick is not self.shorten_paddle \
                and self.brick_offset <= maybe_brick.y <= self.brick_offset+(self.brick_height+self.brick_spacing)*self.brick_rows:
            self.window.remove(maybe_brick)
            self.brick_count += 1
            self.score += self.score_multiple
            if self.double_score_started() is False:
                self.random_item_ds()
            else:
                self.double_score_count += 1
            if self.shorten_paddle_started() is False:
                self.random_item_sp()
            else:
                self.shorten_paddle_count += 1
            self.set_velocity_x()
            self.set_velocity_y()
        maybe_brick = self.window.get_object_at(self.ball.x + self.radius * 2, self.ball.y)
        if maybe_brick is not None and maybe_brick is not self.double_score and maybe_brick is not self.shorten_paddle \
                and self.brick_offset <= maybe_brick.y <= self.brick_offset + (self.brick_height + self.brick_spacing) * self.brick_rows:
            self.window.remove(maybe_brick)
            self.brick_count += 1
            self.score += self.score_multiple
            if self.double_score_started() is False:
                self.random_item_ds()
            else:
                self.double_score_count += 1
            if self.shorten_paddle_started() is False:
                self.random_item_sp()
            else:
                self.shorten_paddle_count += 1
            self.set_velocity_x()
            self.set_velocity_y()
        maybe_brick = self.window.get_object_at(self.ball.x, self.ball.y + self.radius * 2)
        if maybe_brick is not None and maybe_brick is not self.double_score and maybe_brick is not self.shorten_paddle \
                and self.brick_offset <= maybe_brick.y <= self.brick_offset + (self.brick_height + self.brick_spacing) * self.brick_rows:
            self.window.remove(maybe_brick)
            self.brick_count += 1
            self.score += self.score_multiple
            if self.double_score_started() is False:
                self.random_item_ds()
            else:
                self.double_score_count += 1
            if self.shorten_paddle_started() is False:
                self.random_item_sp()
            else:
                self.shorten_paddle_count += 1
            self.set_velocity_x()
            self.set_velocity_y()
        maybe_brick = self.window.get_object_at(self.ball.x + self.radius * 2, self.ball.y + self.radius * 2)
        if maybe_brick is not None and maybe_brick is not self.double_score and maybe_brick is not self.shorten_paddle \
                and self.brick_offset <= maybe_brick.y <= self.brick_offset + (self.brick_height + self.brick_spacing) * self.brick_rows:
            self.window.remove(maybe_brick)
            self.brick_count += 1
            self.score += self.score_multiple
            if self.double_score_started() is False:
                self.random_item_ds()
            else:
                self.double_score_count += 1
            if self.shorten_paddle_started() is False:
                self.random_item_sp()
            else:
                self.shorten_paddle_count += 1
            self.set_velocity_x()
            self.set_velocity_y()

    def bounce(self):
        """Changes ball's direction when hitting the paddle"""
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = -abs(self.__dy)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def check_collision(self):
        """Checking if the ball hit the paddle"""
        if self.window.get_object_at(self.ball.x,self.ball.y+self.radius*2) is self.paddle:
            self.bounce()
        if self.window.get_object_at(self.ball.x+self.radius*2,self.ball.y+self.radius*2) is self.paddle:
            self.bounce()

    def reset_ball(self):
        """Resets the ball when the user loses 1 live"""
        self.window.add(self.ball,x=(self.window.width - self.radius * 2) / 2,
                        y=(self.window.height - self.radius * 2) / 2)
        self.window.add(self.start_label,x=self.window.width/5,y=self.window.height*0.666)
        self.__dx = 0
        self.__dy = 0

    def no_bricks(self):
        """Detecting whether all bricks are cleared"""
        if self.brick_count == self.total_bricks:
            return True
        else:
            return False

    def game_over(self):
        """Notifies the user when game is over"""
        gameover = GLabel('GAME OVER :(')
        gameover.font = '-50'
        self.window.add(gameover,x=self.window.width/6,y=self.window.height*0.666)

    def win_game(self):
        """Notifies the player if he/she removed all bricks"""
        wingame = GLabel('YOU WIN! :D')
        wingame.font = '-50'
        self.window.add(wingame, x=self.window.width / 6, y=self.window.height * 0.666)

    def update_score(self):
        """Updates score label"""
        self.score_label.text = f'Score: {self.score}'

    def random_item_ds(self):
        """Drops a random item that may double score count for limited rounds"""
        if random.random() < 0.3:
            self.window.add(self.double_score, x=self.ball.x+self.objects_length/2, y=self.ball.y)
            self.double_score_exist = True

    def double_score_switch(self):
        """Detects if user catches double score rect"""
        for i in range(int(self.paddle.width)):
            maybe_double = self.window.get_object_at(self.paddle.x + i, self.paddle.y)
            if maybe_double is self.double_score:
                self.window.remove(maybe_double)
                self.double_score_start = True

    def double_score_started(self):
        """Returns True/False if the double score count has started"""
        if self.double_score_start is False:
            return False
        else:
            return True

    def double_score_exec(self):
        """Executes double score for 5 rounds (1 round = 1 brick hit)"""
        if self.double_score_count <= 5:
            self.score_multiple = 2
        else:
            self.score_multiple = 1
            self.double_score_count = 0
            self.double_score_exist = False
            self.double_score_start = False

    def random_item_sp(self):
        """Drops a random item that may shorten the paddle for limited rounds"""
        if random.random() < 0.3:
            self.window.add(self.shorten_paddle, x=self.ball.x+self.objects_length/2, y=self.ball.y)
            self.shorten_paddle_exist = True

    def shorten_paddle_switch(self):
        """Detects if user catches shorten paddle rect"""
        for i in range(self.paddle.width):
            maybe_shorten = self.window.get_object_at(self.paddle.x + i, self.paddle.y)
            if maybe_shorten is self.shorten_paddle:
                self.window.remove(maybe_shorten)
                self.shorten_paddle_start = True

    def shorten_paddle_started(self):
        """Returns True/False if the shorten paddle count has started"""
        if self.shorten_paddle_start is False:
            return False
        else:
            return True

    def shorten_paddle_exec(self):
        """Executes shorten paddle for 5 rounds (1 round = 1 brick hit)"""
        if self.shorten_paddle_count == 0 and self.glitch_count == 1:
            self.window.remove(self.paddle)
            self.paddle = GRect(self.paddle_width-20, self.paddle_height, x=(self.window_width - self.paddle_width) / 2,
                                y=self.window_height - self.paddle_offset)
            self.paddle.color = 'magenta'
            self.paddle.filled = True
            self.paddle.fill_color = 'magenta'
            self.window.add(self.paddle)
            self.glitch_count += 1
        elif 0 < self.shorten_paddle_count <= 5:
            pass
        elif self.shorten_paddle_count > 5:
            self.window.remove(self.paddle)
            self.paddle = GRect(self.paddle_width, self.paddle_height, x=(self.window_width - self.paddle_width) / 2,
                                y=self.window_height - self.paddle_offset)
            self.paddle.color = 'black'
            self.paddle.filled = True
            self.paddle.fill_color = 'black'
            self.window.add(self.paddle)
            self.shorten_paddle_count = 0
            self.shorten_paddle_exist = False
            self.shorten_paddle_start = False
            self.glitch_count = 1
