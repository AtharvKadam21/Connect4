import dearpygui.dearpygui as dpg
#from db import *

dpg.create_context()

with dpg.window(label='Select Mode', modal=True, show=False, tag='b0', no_title_bar=True):
        dpg.add_button(label="VS AI")
        dpg.add_button(label="2 Players")
        dpg.add_button(label="3 Players")
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

    ''' input_txt1=dpg.add_text('Name')
    dpg.set_item_callback(input_txt1, enter_name)'''

with dpg.window(tag="Primary Window"):
    dpg.add_text("Connect 4")
    dpg.add_button(label="Play", callback=lambda: dpg.configure_item('b0', show=True))
    dpg.add_button(label="Account", callback=lambda: dpg.configure_item('b1', show=True))
    dpg.add_button(label="Leaderboard")
    dpg.add_button(label="Quit", callback=lambda: dpg.configure_item('Primary Window', show=False))

dpg.create_viewport(title='Game', width=700, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()