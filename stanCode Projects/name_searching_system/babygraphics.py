"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

FILE: Babygraphics.py
NAME: Sharlene CHen
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    total = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE) - GRAPH_MARGIN_SIZE
    unit = total / len(YEARS)
    return GRAPH_MARGIN_SIZE+unit*year_index


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)    #upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)   #lower line
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH,i),0,get_x_coordinate(CANVAS_WIDTH,i),CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH,i)+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i],anchor=tkinter.NW) #middle lines

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    scale = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK
    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:
            if f'{YEARS[0]}' in name_data[lookup_names[i]]: #text for first point
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 0) + TEXT_DX,
                               GRAPH_MARGIN_SIZE + scale*int((name_data[lookup_names[i]][f'{YEARS[0]}'])),
                               text=f'{lookup_names[i]} {name_data[lookup_names[i]][f"{YEARS[0]}"]}',
                               anchor=tkinter.SW, fill=COLORS[i % 4])
            else:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 0) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=f'{lookup_names[i]} *', anchor=tkinter.SW, fill=COLORS[i % 4])
            for j in range(1,len(YEARS)):   #draws connected lines from this year to last year
                if f'{YEARS[j]}' in name_data[lookup_names[i]] and f'{YEARS[j-1]}' in name_data[lookup_names[i]]:
                    #for the case where names are within max rank for both current and last year
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH,j-1),
                                       GRAPH_MARGIN_SIZE+scale*int(name_data[lookup_names[i]][f'{YEARS[j-1]}']),
                                       get_x_coordinate(CANVAS_WIDTH,j),
                                       GRAPH_MARGIN_SIZE+scale*int(name_data[lookup_names[i]][f'{YEARS[j]}']),
                                       width=LINE_WIDTH,fill=COLORS[i%4]
                                       )
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH,j)+TEXT_DX,
                                       GRAPH_MARGIN_SIZE+scale*int(name_data[lookup_names[i]][f'{YEARS[j]}']),
                                       text=f'{lookup_names[i]} {name_data[lookup_names[i]][f"{YEARS[j]}"]}',
                                       anchor=tkinter.SW,fill=COLORS[i%4])
                elif f'{YEARS[j]}' in name_data[lookup_names[i]] and f'{YEARS[j-1]}' not in name_data[lookup_names[i]]:
                    # for the case where names are within max rank for current but not last year
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j - 1),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, j),
                                       GRAPH_MARGIN_SIZE + scale*int(name_data[lookup_names[i]][f'{YEARS[j]}']),
                                       width=LINE_WIDTH, fill=COLORS[i % 4]
                                       )
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + scale*int(name_data[lookup_names[i]][f'{YEARS[j]}']),
                                       text=f'{lookup_names[i]} {name_data[lookup_names[i]][f"{YEARS[j]}"]}',
                                       anchor=tkinter.SW, fill=COLORS[i % 4])
                else:   # for the case where names are not within max rank
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH,j-1),
                                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,get_x_coordinate(CANVAS_WIDTH,j),
                                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       width=LINE_WIDTH,fill=COLORS[i%4]
                                       )
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH,j)+TEXT_DX,
                                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       text=f'{lookup_names[i]} *', anchor=tkinter.SW,fill=COLORS[i%4])

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
