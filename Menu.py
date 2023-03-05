import dearpygui.dearpygui as dpg
import mysql.connector
import numpy as np
import random
import pygame
import sys
import math

from SinglePlayer import *
from TwoPlayer import *
from ThreePlayer import *


dpg.create_context()
dpg.create_viewport(title='Game', width=700, height=600)
dpg.setup_dearpygui()

def ModeValue(sender, app_data):
    if app_data[1]=='1Play':
        oneplay()
    elif app_data[1]=='2Play':
        twoplay()
    else:
        threeplay()

#=========item_registry==========
with dpg.item_handler_registry(tag="widget handler") as handler:
    dpg.add_item_clicked_handler(callback=ModeValue)

with dpg.window(label='Select Mode', modal=True, show=False, tag='b0', no_title_bar=True):
        dpg.add_button(label="VS AI", tag='1Play')
        dpg.add_button(label="2 Players", tag='2Play')
        dpg.add_button(label="3 Players", tag='3Play')
        dpg.add_button(label="Back", width=75, callback=lambda: dpg.configure_item("b0", show=False))

with dpg.window(label='Account', modal=True, show=False, tag='b1', no_title_bar=True):

    with dpg.group(horizontal=True):
        dpg.add_input_text(default_value="Player")
        dpg.add_button(label="Save")

    with dpg.group(horizontal=True):
        dpg.add_text("Board Theme")
        dpg.add_button(label="Blue")
        dpg.add_button(label="Purple")
      
    with dpg.group(horizontal=True):
        dpg.add_text("Token color")
        dpg.add_button(label="Red")
        dpg.add_button(label="Purple")
    
    dpg.add_button(label="Back", width=75, callback=lambda: dpg.configure_item("b1", show=False))

with dpg.window(tag="Primary Window",width=800, height=600):
    dpg.add_text("Connect 4")
    dpg.add_button(label="Play", callback=lambda: dpg.configure_item('b0', show=True))
    dpg.add_button(label="Account", callback=lambda: dpg.configure_item('b1', show=True))
    dpg.add_button(label="Leaderboard")
    dpg.add_button(label="Quit", callback=lambda: dpg.configure_item('Primary Window', show=False))

#========binding item to registry=========
dpg.bind_item_handler_registry('1Play', "widget handler")
dpg.bind_item_handler_registry('2Play', "widget handler")
dpg.bind_item_handler_registry('3Play', "widget handler")


dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()