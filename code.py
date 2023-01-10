#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Jan. 17th, 2022
# This Program is a gamed called space aliens invasion
# where the player fights off an invasion of space aliens.

# Modules used.
import ugame
import stage


def game_scene():
    # Gets image from file (16x16) and sets it as the stage.
    image_bank_background = stage.Bank.from_bmp16
    ("space_aliens_background.bmp")

    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(image_bank_background, 10, 8)

    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, 60)

    # Creates a list of layers for the game (In order left appear first)
    game.layers = [background]

    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()

    # Place Holder
    while True:
        pass


if __name__ == "__main__":
    game_scene()
