

SIZE = 700                     
                               

CONSTELLATION_FILES = [
    ('Cas_lines.txt', 'white'),
    ('Cyg_lines.txt', 'white'),
    ('BigDipper_lines.txt', 'white'),
    ('Bootes_lines.txt', 'white'),
    ('UrsaMinor_lines.txt', 'white'),
    ('Cepheus_lines.txt', 'white'),
    ('Draco_lines.txt', 'white'),
    ('Auriga_lines.txt', 'white'),
    ('Gemini_lines.txt', 'white')
]




fp = open("stars.txt") #opens the file with all the star data in it

#function 1
def coords_to_pixel(star_x, star_y, size = SIZE):
    '''returns the x, y location of the star in terms of pixels in the picture.'''
    
    m , b = size //2, size //2
    pixel_x = (m * star_x) + b
    pixel_y =(-b * star_y) + m

    return (pixel_x,pixel_y) 


#function 2
def read_stars(fp):
    '''return a tuple of three dictionaries'''
    
    stars_name_andxy = {} #dictionnary 1
    stars_num_and_mag = {} #dictionnary 2
    stars_names_and_mag= {} # dictionnary 3
    for line in fp: #for all the lines in file
        r = line.split(maxsplit=5)
        stars_name_andxy[r[1]] = (float(r[2]),float(r[3]))#assign draper number to tuple of the x,y position
    
        stars_num_and_mag[r[1]]= r[4] #assign draper id as key to its magnitude
    
    
        if len(r) > 5: #if lengnth is bigger than 4, ,eans the tsar has a name
            for name in r[5].split(','):
                fixed_name = name.upper().replace('_', ' ').strip()
            
                stars_names_and_mag[fixed_name]= r[1] #set the star name as key and drapper id as value in dictionnary star_names
        

    return (stars_name_andxy, stars_num_and_mag, stars_names_and_mag) #returns a tuple of 3 dictionnaries



#function 3
def plot_by_magnitude(size, coords, magnitudes):
    for dn in coords:
        x,y = coords[dn]
        x,y = coords_to_pixel(x,y,size)
        c = "white"
        r = 1
        m = magnitudes[dn] #makes magnitude bigger
        draw_star(x,y,r,c)






#function 4
def read_constellation_lines(fp):

    constellations_dict = {}
    for line in fp:
        key = line.split(",")[0].strip() #makes key value first and strips off extra white spaces
        value = line.split(",")[1].strip() #makes second element the value 
        if constellations_dict.get(key) is None:
            constellations_dict[key] = []   #assign an empty list to the key when there's no value
        constellations_dict[key].append(value) 

    return constellations_dict
#x = open("Draco_lines.txt")
#print(read_constellation_lines(fp)) #testing function 5
    
    

    


#function 5
def plot_constellation(coords, lines, names, color, size):
    for s1 in lines: #s1 is star

        for s2 in lines[s1]: #s2 is star
            h1 = names.get(s1,s1)
            h2 = names.get(s2,s2)
            x0,y0 = coords[h1]
            x1,y1 = coords[h2]
            x0,y0 = coords_to_pixel(x0,y0)
            x1,y1 = coords_to_pixel(x1,y1)

            draw_line(x0,y0,x1,y1, "yellow")


def draw_line(x0, y0, x1, y1, color):
    '''Draw a line connecting two points, given integer coordinates for the
    start position (x0, y0) and end position (x1, y1). The color is a string, 
    either a color name (e.g. 'red') or an RGB value '#RRGGBB'.'''
    canvas.create_line(x0, y0, x1, y1, width=1, fill=color)

def draw_star(x, y, radius, color):
    '''Draw a star as a filled circle with a given center (in pixel
    coordinates), radius (in pixels), and color (as above).'''
    if radius < 1:
        canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill=color, width=1)
    else:
        canvas.create_oval(x - radius,
                           y - radius,
                           x + radius,
                           y + radius,fill=color, width=0)

# BASIC TKINTER INITIALIZATION

import tkinter as tk
wnd = tk.Tk()
canvas = tk.Canvas(wnd, width=SIZE, height=SIZE, background='black')
canvas.pack()
wnd.title('Star chart')

# THE MAIN PROGRAM IS HERE (DO NOT CHANGE THIS)!

fp = open('stars.txt')
coords, magnitudes, names = read_stars(fp)
assert len(coords) == len(magnitudes)
print("Read", len(coords), "star coordinates and magnitudes")
print("Read", len(names), "unique star names referring to ", len(set(names.values())), "distinct stars")
fp.close()
plot_by_magnitude(SIZE, coords, magnitudes)
for fname, color in CONSTELLATION_FILES:
    fp = open(fname)
    lines = read_constellation_lines(fp)
    fp.close()
    plot_constellation(coords, lines, names, color, SIZE)


wnd.mainloop()


    
    
