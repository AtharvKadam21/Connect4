import random
import sys
import math

import numpy as np

import dearpygui.dearpygui as dpg
import mysql.connector
import pygame

mydb=mysql.connector.connect(    
    host='localhost',
    user='root',
    password='root123',
    database='connect4')

cur=mydb.cursor()

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

def getdbValues(UserName, BCol, TCol):
    b1=(UserName, BCol, TCol)
    s="INSERT INTO user_accounts VALUES(%s,%s,%s)"
    cur.execute(s,b1)
    mydb.commit()

def dbEntry(sender, app_data, user_data):
    BCol='Blue'
    TCol='Red'
    UserName=dpg.get_value(InName)
    if app_data[1]=='BColBl':
        BCol='Blue'
        print(BCol)        
        
    if app_data[1]=='BColPurp':
        BCol='Purple'
        print(BCol)

    if app_data[1]=='TColRd':
        TCol='Red'
        print(TCol)

    if app_data[1]=='TColPurp':
        TCol='Purple'
        print(TCol)

    getdbValues(UserName, BCol, TCol)

def showldb():
    cur.execute("SELECT * FROM player ORDER BY score DESC")
    rows = cur.fetchall()
    return rows

#=========item_registry(s)==========
with dpg.item_handler_registry(tag="widget handler") as handler:
    dpg.add_item_clicked_handler(callback=ModeValue)

with dpg.item_handler_registry(tag="dbvalues") as handler:
    dpg.add_item_clicked_handler(callback=dbEntry)

with dpg.item_handler_registry(tag="ldb") as handler:
    dpg.add_item_clicked_handler(callback=showldb)

with dpg.window(label='Select Mode', modal=True, show=False, tag='b0', no_title_bar=True,pos=(280,50)):
        dpg.add_button(label="VS AI", tag='1Play',width=100, height=50)
        dpg.add_button(label="2 Players", tag='2Play',width=100, height=50)
        dpg.add_button(label="3 Players", tag='3Play',width=100, height=50)
        dpg.add_button(label="Back", callback=lambda: dpg.configure_item("b0", show=False),width=100, height=50)

with dpg.window(label='Account', modal=True, show=False, tag='b1', no_title_bar=True,pos=(230, 50)):
    with dpg.group(horizontal=True):
        dpg.add_text("Name")
        InName=dpg.add_input_text(default_value="Player", tag="Pname")

    with dpg.group(horizontal=True):
        dpg.add_text("Board Theme")
        dpg.add_button(label="Blue", tag="BColBl", width=100, height=30)
        dpg.add_button(label="Purple", tag="BColPurp", width=100, height=30)

    with dpg.group(horizontal=True):
        dpg.add_text("Token color")
        dpg.add_button(label="Red", tag="TColRd",width=100, height=30)
        dpg.add_button(label="Purple", tag="TColPurp",width=100, height=30)
    
    with dpg.group(horizontal=True):
        dpg.add_button(label="Save", tag="SaveChanges",width=100, height=30)
        dpg.add_button(label="Back", callback=lambda: dpg.configure_item("b1", show=False),width=100, height=30)


with dpg.window(label='Leaderboards', modal=True, show=False, tag='b2', no_title_bar=True, pos=(300, 50)):
    with dpg.group():   
        with dpg.table(header_row=True):
            dpg.add_table_column(label='Name    Score')
            rows=showldb()
            for i in rows:
                print(i)
                with dpg.table_row():
                    dpg.add_text(f"{i[1]}    {i[2]}")   
        dpg.add_button(label="Back", callback=lambda: dpg.configure_item("b2", show=False),width=100, height=30)



with dpg.window(tag="Primary Window", width=700, height=600):
    with dpg.group(pos=(300,50)):
        dpg.add_text("Connect 4")
        dpg.add_button(label="Play", callback=lambda: dpg.configure_item('b0', show=True),width=100, height=40)
        dpg.add_button(label="Account", callback=lambda: dpg.configure_item('b1', show=True),width=100, height=40)
        dpg.add_button(label="Leaderboard", callback=lambda: dpg.configure_item('b2', show=True), width=100, height=40)
        dpg.add_button(label="Quit", callback=lambda: dpg.configure_item('Primary Window', show=False),width=100, height=40)

#========binding item to registry=========
dpg.bind_item_handler_registry('1Play', "widget handler")
dpg.bind_item_handler_registry('2Play', "widget handler")
dpg.bind_item_handler_registry('3Play', "widget handler")

dpg.bind_item_handler_registry('SaveChanges', "dbvalues")
dpg.bind_item_handler_registry('BColBl', "dbvalues")
dpg.bind_item_handler_registry('BColPurp', "dbvalues")

dpg.bind_item_handler_registry('TColRd', "dbvalues")
dpg.bind_item_handler_registry('TColPurp', "dbvalues")

dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()