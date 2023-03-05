import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Game', width=700, height=600)
dpg.setup_dearpygui()

def on_button_press(sender, app_data, user_data):
    selected_color = app_data
    print(f"Selected color: {selected_color}")
    name_value = dpg.get_value("Name Input")
    print(f"Name value: {name_value}")

with dpg.window():
    dpg.add_text("Enter your name:")
    dpg.add_input_text(default_value="Name Input")

    dpg.add_text("Select your favorite color:")
    with dpg.group():
        dpg.add_button(label="Red", callback=on_button_press, callback_data="red")
        dpg.add_button("Green", callback=on_button_press, callback_data="green")
        dpg.add_button("Blue", callback=on_button_press, callback_data="blue")

dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()