#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Jan. 17th, 2023
# This Program is a gamed called space aliens invasion
# where the player fights off an invasion of space aliens.

# Modules used.
import ugame
import stage
import time
import random
import supervisor

import constants

# Splash Scene
def splash_scene():
    # Gets sound ready.
    # Coin sound plays upon splash screen.
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # Gets images from file (16x16) and sets it as the stage.

    # Background
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Sets the background to image 0 in the image bank.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Tiles the background in the splash screen.
    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)

    # Creates a list of layers for the game (In order left appear first)
    game.layers = [background]

    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()

    # Repeat forever , game loop.
    while True:
        # Wait 2 seconds.
        time.sleep(2.0)
        menu_scene()


# Menu Scene
def menu_scene():
    # Gets images from file (16x16) and sets it as the stage.

    # Background
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("Tamer Studios")
    text.append(text1)
    # Text Displaying Press Start
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(20, 110)
    text2.text("PRESS START\nTO PLAY")
    text.append(text2)
    # Text Displaying A = HARD B = EASY
    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(20, 50)
    text3.text("A = HARD B = EASY")
    text.append(text3)
    # Text Displaying Press Up To Open
    tex4 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    tex4.move(20, 80)
    tex4.text("Press UP\nTo Open Tutorial")
    text.append(tex4)
    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)

    # Creates a list of layers for the game (In order left appear first)
    game.layers = text + [background]

    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()
    # initializes a and b buttons to 0.
    a_button = 0
    b_button = 0
    easy_mode_state = False
    # Place Holder
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # A button state.
        if keys & ugame.K_X != 0:
            a_button = constants.button_state["button_just_pressed"]
        # B button state.
        if keys & ugame.K_O != 0:
            b_button = constants.button_state["button_just_pressed"]
        if a_button == constants.button_state["button_just_pressed"]:
            easy_mode_state = True
        if b_button == constants.button_state["button_just_pressed"]:
            easy_mode_state = False
        if keys & ugame.K_UP != 0:
            tutorial(easy_mode_state)
        if keys & ugame.K_START != 0:
            game_scene(easy_mode_state)
        # Update game logic.

        # Redraw sprites
        game.tick()


def game_scene(easy_mode):

    # For Score
    score = 0
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))
    # Ship/Player Lives
    ship_lives = 3
    # Text Displayed for ship lives.
    ship_lives_text = stage.Text(width=29, height=14)
    ship_lives_text.clear()
    ship_lives_text.cursor(0, 0)
    ship_lives_text.move(1, 10)
    ship_lives_text.text("Lives: {0}".format(ship_lives))

    def show_alien():
        # This function takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    # Gets images from file (16x16) and sets it as the stage.

    # Background
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Sprite
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Buttons state information.
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]

    # get sound file ready.
    pew_sound = open("pew.wav", "rb")
    boom_sound = open("boom.wav", "rb")
    crash_sound = open("crash.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # For loop to randomise tiles in background.
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    # Initializes the ship variable to a sprite from image bank sprites and gets the fifth image.
    ship = stage.Sprite(
        image_bank_sprites, 4, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    # Initializes the alien variable to a sprite from image bank sprites and gets the 9th image.
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        aliens.append(a_single_alien)
    # Place An Alien on the Screen.
    show_alien()

    # Create a list of lasers for shooting.
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)

    # Creates a list of layers for the game (In order left appear first)

    game.layers = (
        [ship_lives_text] + [score_text] + aliens + lasers + [ship] + [background]
    )

    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()

    # Place Holder
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_O:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        # Move up if easy mode is true.
        if keys & ugame.K_UP:
            if easy_mode == True:
                if ship.y > 0:
                    ship.move(ship.x, ship.y - 1)
                else:
                    ship.move(ship.x, 0)
            else:
                pass
        # Move down if easy mode is true.
        if keys & ugame.K_DOWN:
            if easy_mode == True:
                if ship.y < 100:
                    ship.move(ship.x, ship.y + 1)
                else:
                    ship.move(ship.x, 100)
            else:
                pass
        # Move right.
        if keys & ugame.K_RIGHT:
            # Boost given to player if they press b.
            if b_button == constants.button_state["button_still_pressed"]:
                if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                    ship.move(ship.x + (constants.SPRITE_MOVEMENT_SPEED + 1), ship.y)
                else:
                    ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            # If player does not press b.
            else:
                if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                    ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
                else:
                    ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            # Boost given to player if they press b.
            if b_button == constants.button_state["button_still_pressed"]:
                if ship.x >= 0:
                    ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED - 1, ship.y)
                else:
                    ship.move(0, ship.y)
            # If player does not press b.
            else:
                if ship.x >= 0:
                    ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
                else:
                    ship.move(0, ship.y)
        # Update game logic.

        # Play sound if A button was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # Fire a laser if we have enough power (if we have available lasers)
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        # Each frame move the laser that has been fired up.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # Each frame move aliens down.
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    show_alien()
                    # Brings the player score down if the aliens go off screen.
                    score -= 1
                    if score < 0:
                        score = 0
                    # Displays Score.
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # Check for collision between Laser and alien.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        # If the lasers collide with the aliens/
                        if stage.collide(
                            lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x + 1,
                            aliens[alien_number].y,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15,
                        ):
                            # You hit an alien.
                            aliens[alien_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            sound.stop()
                            sound.play(boom_sound)
                            # Puts more aliens on screen.
                            show_alien()
                            show_alien()
                            # Update score.
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
        # Check if any aliens are touching the spaceship.
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                # If an Alien colides with a ship.
                if stage.collide(
                    aliens[alien_number].x + 1,
                    aliens[alien_number].y,
                    aliens[alien_number].x + 15,
                    aliens[alien_number].y + 15,
                    ship.x,
                    ship.y,
                    ship.x + 15,
                    ship.y + 15,
                ):
                    # Puts The Aliens Off Screen.
                    for alien_number in range(5):
                        (aliens[alien_number]).move(
                            constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                        )
                        # Puts the aliens on screen.
                        show_alien()
                        show_alien()
                    # Remove one life.
                    ship_lives -= 1
                    sound.play(crash_sound)
                    ship_lives_text.clear()
                    ship_lives_text.cursor(0, 0)
                    ship_lives_text.move(1, 10)
                    ship_lives_text.text("Lives: {0}".format(ship_lives))
                    # Put ship on screen on a random x axis.
                    ship.move(random.randint(0, constants.SCREEN_X), ship.y)
                    if ship_lives == 0:
                        ship_lives_text.clear()
                        ship_lives_text.cursor(0, 0)
                        ship_lives_text.move(1, 10)
                        ship_lives_text.text("Lives: {0}".format(ship_lives))
                        sound.stop()
                        sound.play(crash_sound)
                        time.sleep(3.0)
                        # Calls the function to end game.
                        game_over_scene(score)

        # Redraw sprites
        game.render_sprites(aliens + lasers + [ship])
        game.tick()


def game_over_scene(final_score):
    # Function for game over scene.

    # Image Bank For Final Scene
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Sets the background to image 0 in the image bank
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects

    text = []
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None
    )
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None
    )
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None
    )
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FP5)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input

        keys = ugame.buttons.get_pressed()

        # Start button selected

        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
        # update game logic
        game.tick()  # wait until refresh rate finishes


def tutorial(easy_mode_state):
    # Gets images from file (16x16) and sets it as the stage.
    # Background
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(15, 10)
    text1.text("DOWN = PLAY")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(15, 50)
    text2.text("B = Shoot")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(15, 30)
    text3.text("A = Boost")
    text.append(text3)
    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)

    # Creates a list of layers for the game (In order left appear first)
    game.layers = text + [background]

    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()

    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_DOWN != 0:
            game_scene(easy_mode_state)
        # Update game logic.

        # Redraw sprites
        game.tick()


if __name__ == "__main__":
    splash_scene()
