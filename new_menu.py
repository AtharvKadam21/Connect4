import dearpygui.dearpygui as dpg
import mysql.connector
from G13A_copy import *


dpg.create_context()
dpg.create_viewport(title='Game', width=700, height=600)
dpg.setup_dearpygui()

def getSinglePlayer(sender, app_data):
    single_player()

def getTwoPlayers(sender, app_data):
    two_players()

def getThreePlayers(sender, app_data):
    three_players()


#=========item_registry==========
with dpg.item_handler_registry(tag="widget handler") as handler:
    dpg.add_item_clicked_handler(callback=getSinglePlayer)
    dpg.add_item_clicked_handler(callback=getTwoPlayers)
    dpg.add_item_clicked_handler(callback=getThreePlayers)

with dpg.window(label='Select Mode', modal=True, show=False, tag='b0', no_title_bar=True):
        dpg.add_button(label="VS AI", tag='1Play')
        dpg.add_button(label="2 Players", callback='getTwoPlayers', tag='2Play')
        dpg.add_button(label="3 Players", callback='getThreePlayers', tag='3Play')
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

with dpg.window(tag="Primary Window"):
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