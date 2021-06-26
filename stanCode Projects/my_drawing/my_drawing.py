"""
File: My Drawing
Name: Sharlene
----------------------
TODO: Creates a beautiful photographic image of my college Cornell :)
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GArc, GLabel


def main():
    """
    TODO: Creates a beautiful photographic image of my college Cornell bit by bit.
    """
    window = GWindow(1000,800,title="Sharlene_Drawing")
    background = GRect(1000,800,x=0,y=0) #prints the sky blue
    background.filled = True
    background.fill_color='azure'
    window.add(background)
    ground = GRect(window.width, window.height/2,x=0,y=window.height/2)
    ground.color = 'azure'
    ground.filled = True
    ground.fill_color = 'white'
    window.add(ground)
    snowhill = GArc(600, 200, 180, 190, 650, 330)
    snowhill.filled = True
    snowhill.color = 'silver'
    snowhill.fill_color = "silver"
    window.add(snowhill)
    #building and roofs are colored from the right to the left
    roof_1 = GPolygon()
    roof_1.add_vertex((660,250))
    roof_1.add_vertex((610,250))
    roof_1.add_vertex((635,200))
    roof_1.filled = True
    roof_1.fill_color = "darkcyan"
    window.add(roof_1)
    building_1 = GRect(50,150,x=610,y=250)
    building_1.filled = True
    building_1.fill_color = 'sienna'
    window.add(building_1)
    wall_1 = GRect(40,150,x=570,y=250)
    wall_1.filled = True
    wall_1.fill_color = "saddlebrown"
    window.add(wall_1)
    upperroof_1 = GPolygon()
    upperroof_1.add_vertex((635,200))
    upperroof_1.add_vertex((610,250))
    upperroof_1.add_vertex((570,250))
    upperroof_1.add_vertex((545,200))
    upperroof_1.filled = True
    upperroof_1.fill_color = "teal"
    window.add(upperroof_1)
    roof_2 = GPolygon()
    roof_2.add_vertex((570,250))
    roof_2.add_vertex((440,250))
    roof_2.add_vertex((505,120))
    roof_2.filled = True
    roof_2.fill_color = "darkcyan"
    window.add(roof_2)
    building_2= GRect(130,150,x=440,y=250)
    building_2.filled = True
    building_2.fill_color = 'sienna'
    window.add(building_2)
    upperroof_2 = GPolygon()
    upperroof_2.add_vertex((440,250))
    upperroof_2.add_vertex((465,200))
    upperroof_2.add_vertex((100,200))
    upperroof_2.add_vertex((150,250))
    upperroof_2.filled = True
    upperroof_2.fill_color = "darkslategray"
    window.add(upperroof_2)
    building_3 = GRect(290,150,x=150,y=250)
    building_3.filled = True
    building_3.fill_color = 'saddlebrown'
    window.add(building_3)
    roof_3 = GPolygon()
    roof_3.add_vertex((150,250))
    roof_3.add_vertex((10, 250))
    roof_3.add_vertex((80, 180))
    roof_3.filled = True
    roof_3.fill_color = "darkcyan"
    window.add(roof_3)
    building_4 = GRect(140,150,x=10,y=250)
    building_4.filled = True
    building_4.fill_color = 'chocolate'
    window.add(building_4)
    wallwindow_bigoval_1 = GArc(30,70,0,180)
    wallwindow_bigoval_1.filled = True
    wallwindow_bigoval_1.fill_color = 'darkslategrey'
    window.add(wallwindow_bigoval_1,x=90,y=270)
    wallwindow_bigoval_2 = GArc(30, 70, 0, 180)
    wallwindow_bigoval_2.filled = True
    wallwindow_bigoval_2.fill_color = 'darkslategrey'
    window.add(wallwindow_bigoval_2,x=30,y=270)
    wallwindow_bigrect_1 = GRect(30,50,x=30,y=285)
    wallwindow_bigrect_1.filled = True
    wallwindow_bigrect_1.fill_color = 'darkgrey'
    wallwindow_bigrect_2 = GRect(30,50,x=90,y=285)
    wallwindow_bigrect_2.filled = True
    wallwindow_bigrect_2.fill_color = 'darkgrey'
    window.add(wallwindow_bigrect_1)
    window.add(wallwindow_bigrect_2)
    wallwindow_small_1 = GRect(30,30)
    wallwindow_small_1.filled = True
    wallwindow_small_1.fill_color = 'silver'
    wallwindow_small_2 = GRect(30,30)
    wallwindow_small_2.filled = True
    wallwindow_small_2.fill_color = 'silver'
    window.add(wallwindow_small_1,x=30,y=350)
    window.add(wallwindow_small_2,x=90,y=350)
    roofwindow_tri_1 = GPolygon()
    roofwindow_tri_1.add_vertex((175,210))
    roofwindow_tri_1.add_vertex((160,220))
    roofwindow_tri_1.add_vertex((190,220))
    roofwindow_tri_1.filled = True
    roofwindow_tri_1.color = 'black'
    roofwindow_tri_1.fill_color = "darkgray"
    window.add(roofwindow_tri_1)
    roofwindow_tri_2 = GPolygon()
    roofwindow_tri_2.add_vertex((235, 210))
    roofwindow_tri_2.add_vertex((220, 220))
    roofwindow_tri_2.add_vertex((250, 220))
    roofwindow_tri_2.filled = True
    roofwindow_tri_2.color = 'black'
    roofwindow_tri_2.fill_color = "darkgray"
    window.add(roofwindow_tri_2)
    roofwindow_tri_3 = GPolygon()
    roofwindow_tri_3.add_vertex((295, 210))
    roofwindow_tri_3.add_vertex((280, 220))
    roofwindow_tri_3.add_vertex((310, 220))
    roofwindow_tri_3.filled = True
    roofwindow_tri_3.color = 'black'
    roofwindow_tri_3.fill_color = "darkgray"
    window.add(roofwindow_tri_3)
    roofwindow_tri_4 = GPolygon()
    roofwindow_tri_4.add_vertex((355, 210))
    roofwindow_tri_4.add_vertex((340, 220))
    roofwindow_tri_4.add_vertex((370, 220))
    roofwindow_tri_4.filled = True
    roofwindow_tri_4.color = 'black'
    roofwindow_tri_4.fill_color = "darkgray"
    window.add(roofwindow_tri_4)
    roofwindow_tri_5 = GPolygon()
    roofwindow_tri_5.add_vertex((415, 210))
    roofwindow_tri_5.add_vertex((400, 220))
    roofwindow_tri_5.add_vertex((430, 220))
    roofwindow_tri_5.filled = True
    roofwindow_tri_5.color = 'black'
    roofwindow_tri_5.fill_color = "darkgray"
    window.add(roofwindow_tri_5)
    roofwindow_sq_1 = GRect(30,15)
    roofwindow_sq_2 = GRect(30, 15)
    roofwindow_sq_3 = GRect(30, 15)
    roofwindow_sq_4 = GRect(30, 15)
    roofwindow_sq_5 = GRect(30, 15)
    roofwindow_sq_1.filled = True
    roofwindow_sq_1.color = 'black'
    roofwindow_sq_1.fill_color = "steelblue"
    roofwindow_sq_2.filled = True
    roofwindow_sq_2.color = 'black'
    roofwindow_sq_2.fill_color = "steelblue"
    roofwindow_sq_3.filled = True
    roofwindow_sq_3.color = 'black'
    roofwindow_sq_3.fill_color = "steelblue"
    roofwindow_sq_4.filled = True
    roofwindow_sq_4.color = 'black'
    roofwindow_sq_4.fill_color = "steelblue"
    roofwindow_sq_5.filled = True
    roofwindow_sq_5.color = 'black'
    roofwindow_sq_5.fill_color = "steelblue"
    window.add(roofwindow_sq_1, x=160,y=220)
    window.add(roofwindow_sq_2, x=220, y=220)
    window.add(roofwindow_sq_3, x=280, y=220)
    window.add(roofwindow_sq_4, x=340, y=220)
    window.add(roofwindow_sq_5, x=400, y=220)
    smallarcwindow_1 = GArc(15,30,0,180,x=160,y=300)
    smallarcwindow_2 = GArc(15,30,0,180,x=180,y=300)
    smallarcwindow_3 = GArc(15, 30, 0, 180, x=220, y=300)
    smallarcwindow_4 = GArc(15, 30, 0, 180, x=240, y=300)
    smallarcwindow_5 = GArc(15, 30, 0, 180, x=280, y=300)
    smallarcwindow_6 = GArc(15, 30, 0, 180, x=300, y=300)
    smallarcwindow_7 = GArc(15, 30, 0, 180, x=340, y=300)
    smallarcwindow_8 = GArc(15, 30, 0, 180, x=360, y=300)
    smallarcwindow_9 = GArc(15, 30, 0, 180, x=400, y=300)
    smallarcwindow_10 = GArc(15, 30, 0, 180, x=420, y=300)
    smallarcwindow_1.filled = True
    smallarcwindow_1.fill_color = 'darkslategray'
    smallarcwindow_2.filled = True
    smallarcwindow_2.fill_color = 'darkslategray'
    smallarcwindow_3.filled = True
    smallarcwindow_3.fill_color = 'darkslategray'
    smallarcwindow_4.filled = True
    smallarcwindow_4.fill_color = 'darkslategray'
    smallarcwindow_5.filled = True
    smallarcwindow_5.fill_color = 'darkslategray'
    smallarcwindow_6.filled = True
    smallarcwindow_6.fill_color = 'darkslategray'
    smallarcwindow_7.filled = True
    smallarcwindow_7.fill_color = 'darkslategray'
    smallarcwindow_8.filled = True
    smallarcwindow_8.fill_color = 'darkslategray'
    smallarcwindow_9.filled = True
    smallarcwindow_9.fill_color = 'darkslategray'
    smallarcwindow_10.filled = True
    smallarcwindow_10.fill_color = 'darkslategray'
    window.add(smallarcwindow_1)
    window.add(smallarcwindow_2)
    window.add(smallarcwindow_3)
    window.add(smallarcwindow_4)
    window.add(smallarcwindow_5)
    window.add(smallarcwindow_6)
    window.add(smallarcwindow_7)
    window.add(smallarcwindow_8)
    window.add(smallarcwindow_9)
    window.add(smallarcwindow_10)
    smallrectwindow_1 = GRect(15,30,x=160,y=305)
    smallrectwindow_2 = GRect(15,30, x=180, y=305)
    smallrectwindow_3 = GRect(15, 30, x=220, y=305)
    smallrectwindow_4 = GRect(15, 30, x=240, y=305)
    smallrectwindow_5 = GRect(15, 30, x=280, y=305)
    smallrectwindow_6 = GRect(15, 30, x=300, y=305)
    smallrectwindow_7 = GRect(15, 30, x=340, y=305)
    smallrectwindow_8 = GRect(15, 30, x=360, y=305)
    smallrectwindow_9 = GRect(15, 30, x=400, y=305)
    smallrectwindow_10 = GRect(15, 30, x=420, y=305)
    smallrectwindow_1.filled = True
    smallrectwindow_1.fill_color = 'darkgray'
    smallrectwindow_2.filled = True
    smallrectwindow_2.fill_color = 'darkgray'
    smallrectwindow_3.filled = True
    smallrectwindow_3.fill_color = 'darkgray'
    smallrectwindow_4.filled = True
    smallrectwindow_4.fill_color = 'darkgray'
    smallrectwindow_5.filled = True
    smallrectwindow_5.fill_color = 'darkgray'
    smallrectwindow_6.filled = True
    smallrectwindow_6.fill_color = 'darkgray'
    smallrectwindow_7.filled = True
    smallrectwindow_7.fill_color = 'darkgray'
    smallrectwindow_8.filled = True
    smallrectwindow_8.fill_color = 'darkgray'
    smallrectwindow_9.filled = True
    smallrectwindow_9.fill_color = 'darkgray'
    smallrectwindow_10.filled = True
    smallrectwindow_10.fill_color = 'darkgray'
    window.add(smallrectwindow_1)
    window.add(smallrectwindow_2)
    window.add(smallrectwindow_3)
    window.add(smallrectwindow_4)
    window.add(smallrectwindow_5)
    window.add(smallrectwindow_6)
    window.add(smallrectwindow_7)
    window.add(smallrectwindow_8)
    window.add(smallrectwindow_9)
    window.add(smallrectwindow_10)
    lowerwindow_1 = GRect(15,15,x=160,y=350)
    lowerwindow_2 = GRect(15, 15, x=160, y=365)
    lowerwindow_3 = GRect(15, 15, x=180, y=350)
    lowerwindow_4 = GRect(15, 15, x=180, y=365)
    lowerwindow_5 = GRect(15, 15, x=220, y=350)
    lowerwindow_6 = GRect(15, 15, x=220, y=365)
    lowerwindow_7 = GRect(15, 15, x=240, y=350)
    lowerwindow_8 = GRect(15, 15, x=240, y=365)
    lowerwindow_9 = GRect(15, 15, x=280, y=350)
    lowerwindow_10 = GRect(15, 15, x=280, y=365)
    lowerwindow_11 = GRect(15, 15, x=300, y=350)
    lowerwindow_12 = GRect(15, 15, x=300, y=365)
    lowerwindow_13 = GRect(15, 15, x=340, y=350)
    lowerwindow_14 = GRect(15, 15, x=340, y=365)
    lowerwindow_15 = GRect(15, 15, x=360, y=350)
    lowerwindow_16 = GRect(15, 15, x=360, y=365)
    lowerwindow_17 = GRect(15, 15, x=400, y=350)
    lowerwindow_18 = GRect(15, 15, x=400, y=365)
    lowerwindow_19 = GRect(15, 15, x=420, y=350)
    lowerwindow_20 = GRect(15, 15, x=420, y=365)
    lowerwindow_1.filled = True
    lowerwindow_1.fill_color = 'silver'
    lowerwindow_2.filled = True
    lowerwindow_2.fill_color = 'silver'
    lowerwindow_3.filled = True
    lowerwindow_3.fill_color = 'silver'
    lowerwindow_4.filled = True
    lowerwindow_4.fill_color = 'silver'
    lowerwindow_5.filled = True
    lowerwindow_5.fill_color = 'silver'
    lowerwindow_6.filled = True
    lowerwindow_6.fill_color = 'silver'
    lowerwindow_7.filled = True
    lowerwindow_7.fill_color = 'silver'
    lowerwindow_8.filled = True
    lowerwindow_8.fill_color = 'silver'
    lowerwindow_9.filled = True
    lowerwindow_9.fill_color = 'silver'
    lowerwindow_10.filled = True
    lowerwindow_10.fill_color = 'silver'
    lowerwindow_11.filled = True
    lowerwindow_11.fill_color = 'silver'
    lowerwindow_12.filled = True
    lowerwindow_12.fill_color = 'silver'
    lowerwindow_13.filled = True
    lowerwindow_13.fill_color = 'silver'
    lowerwindow_14.filled = True
    lowerwindow_14.fill_color = 'silver'
    lowerwindow_15.filled = True
    lowerwindow_15.fill_color = 'silver'
    lowerwindow_16.filled = True
    lowerwindow_16.fill_color = 'silver'
    lowerwindow_17.filled = True
    lowerwindow_17.fill_color = 'silver'
    lowerwindow_18.filled = True
    lowerwindow_18.fill_color = 'silver'
    lowerwindow_19.filled = True
    lowerwindow_19.fill_color = 'silver'
    lowerwindow_20.filled = True
    lowerwindow_20.fill_color = 'silver'
    window.add(lowerwindow_1)
    window.add(lowerwindow_2)
    window.add(lowerwindow_3)
    window.add(lowerwindow_4)
    window.add(lowerwindow_5)
    window.add(lowerwindow_6)
    window.add(lowerwindow_7)
    window.add(lowerwindow_8)
    window.add(lowerwindow_9)
    window.add(lowerwindow_10)
    window.add(lowerwindow_11)
    window.add(lowerwindow_12)
    window.add(lowerwindow_13)
    window.add(lowerwindow_14)
    window.add(lowerwindow_15)
    window.add(lowerwindow_16)
    window.add(lowerwindow_17)
    window.add(lowerwindow_18)
    window.add(lowerwindow_19)
    window.add(lowerwindow_20)
    doorarc = GArc(50,100,0,180,x=480,y=325)
    doorarc.filled = True
    doorarc.fill_color = 'saddlebrown'
    door = GRect(50, 50, x=480, y=350)
    door.filled = True
    door.fill_color = 'orangered'
    window.add(doorarc)
    window.add(door)
    mainarc_1 =GArc(25,80,0,180,x=460,y=270)
    mainarc_1.filled = True
    mainarc_1.fill_color = 'darkslategray'
    window.add(mainarc_1)
    mainarc_2 =GArc(25,80,0,180,x=525,y=270)
    mainarc_2.filled = True
    mainarc_2.fill_color = 'darkslategray'
    window.add(mainarc_2)
    mainsquare_1 = GRect(25,30,x=460,y=290)
    mainsquare_1.filled = True
    mainsquare_1.fill_color = 'darkgray'
    mainsquare_2 = GRect(25,30,x=525,y=290)
    mainsquare_2.filled = True
    mainsquare_2.fill_color = 'darkgray'
    window.add(mainsquare_1)
    window.add(mainsquare_2)
    sidearc_1 = GArc(15,80,0,180,x=615,y=270)
    sidearc_1.filled = True
    sidearc_1.fill_color = 'darkslategray'
    window.add(sidearc_1)
    sidearc_2 = GArc(15, 80, 0, 180, x=640, y=270)
    sidearc_2.filled = True
    sidearc_2.fill_color = 'darkslategray'
    window.add(sidearc_2)
    sidesquare_1 = GRect(15,60,x=615,y=285)
    sidesquare_1.filled = True
    sidesquare_1.fill_color = 'darkgray'
    window.add(sidesquare_1)
    sidesquare_2 = GRect(15, 60, x=640, y=285)
    sidesquare_2.filled = True
    sidesquare_2.fill_color = 'darkgray'
    window.add(sidesquare_2)
    sun = GOval(100,100,x=750,y=200)
    sun.filled = True
    sun.color = 'lightgoldenrodyellow'
    sun.fill_color = 'lightgoldenrodyellow'
    window.add(sun)
    sunlight_1 = GPolygon()
    sunlight_1.add_vertex((715, 190))
    sunlight_1.add_vertex((735, 212))
    sunlight_1.add_vertex((742, 207))
    sunlight_1.add_vertex((722, 185))
    sunlight_1.filled = True
    sunlight_1.color = 'orange'
    sunlight_1.fill_color = 'orange'
    window.add(sunlight_1)
    sunlight_2 = GPolygon()
    sunlight_2.add_vertex((715, 307))
    sunlight_2.add_vertex((735, 285))
    sunlight_2.add_vertex((742, 290))
    sunlight_2.add_vertex((722, 312))
    sunlight_2.filled = True
    sunlight_2.color = 'orange'
    sunlight_2.fill_color = 'orange'
    window.add(sunlight_2)
    sunlight_3 = GPolygon()
    sunlight_3.add_vertex((865, 290))
    sunlight_3.add_vertex((885, 312))
    sunlight_3.add_vertex((892, 307))
    sunlight_3.add_vertex((872, 285))
    sunlight_3.filled = True
    sunlight_3.color = 'orange'
    sunlight_3.fill_color = 'orange'
    window.add(sunlight_3)
    sunlight_4 = GPolygon()
    sunlight_4.add_vertex((892, 190))
    sunlight_4.add_vertex((872, 212))
    sunlight_4.add_vertex((865, 207))
    sunlight_4.add_vertex((885, 185))
    sunlight_4.filled = True
    sunlight_4.color = 'orange'
    sunlight_4.fill_color = 'orange'
    window.add(sunlight_4)
    sunlight_5 = GRect(10,40,x=795,y=140)
    sunlight_5.filled = True
    sunlight_5.color = 'yellow'
    sunlight_5.fill_color = 'yellow'
    window.add(sunlight_5)
    sunlight_6 = GRect(10,40,x=795,y=320)
    sunlight_6.filled = True
    sunlight_6.color = 'yellow'
    sunlight_6.fill_color = 'yellow'
    window.add(sunlight_6)
    sunlight_7 = GRect(40,10,x=695,y=250)
    sunlight_7.filled = True
    sunlight_7.color = 'yellow'
    sunlight_7.fill_color = 'yellow'
    window.add(sunlight_7)
    sunlight_8 = GRect(40,10,x=870,y=250)
    sunlight_8.filled = True
    sunlight_8.color = 'yellow'
    sunlight_8.fill_color = 'yellow'
    window.add(sunlight_8)
    footstep_1 = GOval(10, 30, x=50, y=450)
    footstep_1.filled = True
    footstep_1.color = 'silver'
    footstep_1.fill_color = 'silver'
    window.add(footstep_1)
    footstep_2 = GOval(10, 30, x=70, y=450)
    footstep_2.filled = True
    footstep_2.color = 'silver'
    footstep_2.fill_color = 'silver'
    window.add(footstep_2)
    footstep_3 = GOval(10, 30, x=100, y=500)
    footstep_3.filled = True
    footstep_3.color = 'silver'
    footstep_3.fill_color = 'silver'
    window.add(footstep_3)
    footstep_4 = GOval(10, 30, x=120, y=500)
    footstep_4.filled = True
    footstep_4.color = 'silver'
    footstep_4.fill_color = 'silver'
    window.add(footstep_4)
    footstep_5 = GOval(10, 30, x=150, y=550)
    footstep_5.filled = True
    footstep_5.color = 'silver'
    footstep_5.fill_color = 'silver'
    window.add(footstep_5)
    footstep_6 = GOval(10, 30, x=170, y=550)
    footstep_6.filled = True
    footstep_6.color = 'silver'
    footstep_6.fill_color = 'silver'
    window.add(footstep_6)
    footstep_7 = GOval(10,30,x=200,y=650)
    footstep_7.filled = True
    footstep_7.color = 'silver'
    footstep_7.fill_color = 'silver'
    window.add(footstep_7)
    footstep_8 = GOval(10, 30, x=220, y=650)
    footstep_8.filled = True
    footstep_8.color = 'silver'
    footstep_8.fill_color = 'silver'
    window.add(footstep_8)
    footstep_9 = GOval(10, 30, x=550, y=550)
    footstep_9.filled = True
    footstep_9.color = 'silver'
    footstep_9.fill_color = 'silver'
    window.add(footstep_9)
    footstep_10 = GOval(10, 30, x=570, y=550)
    footstep_10.filled = True
    footstep_10.color = 'silver'
    footstep_10.fill_color = 'silver'
    window.add(footstep_10)
    footstep_11 = GOval(10, 30, x=600, y=600)
    footstep_11.filled = True
    footstep_11.color = 'silver'
    footstep_11.fill_color = 'silver'
    window.add(footstep_11)
    footstep_12 = GOval(10, 30, x=620, y=600)
    footstep_12.filled = True
    footstep_12.color = 'silver'
    footstep_12.fill_color = 'silver'
    window.add(footstep_12)
    footstep_13 = GOval(10, 30, x=650, y=650)
    footstep_13.filled = True
    footstep_13.color = 'silver'
    footstep_13.fill_color = 'silver'
    window.add(footstep_13)
    footstep_14 = GOval(10, 30, x=670, y=650)
    footstep_14.filled = True
    footstep_14.color = 'silver'
    footstep_14.fill_color = 'silver'
    window.add(footstep_14)
    footstep_15 = GOval(10, 30, x=700, y=750)
    footstep_15.filled = True
    footstep_15.color = 'silver'
    footstep_15.fill_color = 'silver'
    window.add(footstep_15)
    footstep_16 = GOval(10, 30, x=720, y=750)
    footstep_16.filled = True
    footstep_16.color = 'silver'
    footstep_16.fill_color = 'silver'
    window.add(footstep_16)
    treetrunk_1 = GPolygon()
    treetrunk_1.add_vertex((330,600))
    treetrunk_1.add_vertex((350,570))
    treetrunk_1.add_vertex((150,400))
    treetrunk_1.add_vertex((90,350))
    treetrunk_1.filled = True
    treetrunk_1.color = 'sienna'
    treetrunk_1.fill_color = 'sienna'
    window.add(treetrunk_1)
    treetrunk_2 = GRect(30,500,x=330,y=300)
    treetrunk_2.filled = True
    treetrunk_2.color = 'sienna'
    treetrunk_2.fill_color = 'sienna'
    window.add(treetrunk_2)
    treebranch_1= GPolygon()
    treebranch_1.add_vertex((360,420))
    treebranch_1.add_vertex((360,450))
    treebranch_1.add_vertex((390,330))
    treebranch_1.filled = True
    treebranch_1.color = 'sienna'
    treebranch_1.fill_color = 'sienna'
    window.add(treebranch_1)
    treebranch_2 = GPolygon()
    treebranch_2.add_vertex((160, 420))
    treebranch_2.add_vertex((182, 450))
    treebranch_2.add_vertex((190, 330))
    treebranch_2.filled = True
    treebranch_2.color = 'sienna'
    treebranch_2.fill_color = 'sienna'
    window.add(treebranch_2)
    treebranch_3 = GPolygon()
    treebranch_3.add_vertex((290, 550))
    treebranch_3.add_vertex((270, 530))
    treebranch_3.add_vertex((150, 600))
    treebranch_3.filled = True
    treebranch_3.color = 'sienna'
    treebranch_3.fill_color = 'sienna'
    window.add(treebranch_3)
    treeroot_1 = GOval(150,150,x=275,y=750)
    treeroot_1.filled = True
    treeroot_1.color = 'saddlebrown'
    treeroot_1.fill_color = 'saddlebrown'
    window.add(treeroot_1)
    treeroot_2 = GArc(150, 150, 0,180, x=775, y=550)
    treeroot_2.filled = True
    treeroot_2.color = 'saddlebrown'
    treeroot_2.fill_color = 'saddlebrown'
    window.add(treeroot_2)
    treetrunk_3 = GRect(30,300,x=850,y=275)
    treetrunk_3.filled = True
    treetrunk_3.color = 'sienna'
    treetrunk_3.fill_color = 'sienna'
    window.add(treetrunk_3)
    treebranch_4 = GPolygon()
    treebranch_4.add_vertex((880, 450))
    treebranch_4.add_vertex((870, 430))
    treebranch_4.add_vertex((750, 500))
    treebranch_4.filled = True
    treebranch_4.color = 'sienna'
    treebranch_4.fill_color = 'sienna'
    window.add(treebranch_4)
    treebranch_5 = GPolygon()
    treebranch_5.add_vertex((870, 400))
    treebranch_5.add_vertex((982, 350))
    treebranch_5.add_vertex((870, 430))
    treebranch_5.filled = True
    treebranch_5.color = 'sienna'
    treebranch_5.fill_color = 'sienna'
    window.add(treebranch_5)
    treebranch_6 = GPolygon()
    treebranch_6.add_vertex((870, 350))
    treebranch_6.add_vertex((770, 300))
    treebranch_6.add_vertex((850, 380))
    treebranch_6.filled = True
    treebranch_6.color = 'sienna'
    treebranch_6.fill_color = 'sienna'
    window.add(treebranch_6)
    name = GLabel('stanCode x Sharlene', x = 700, y = 750)
    name.font = '-30'
    window.add(name)

if __name__ == '__main__':
    main()
