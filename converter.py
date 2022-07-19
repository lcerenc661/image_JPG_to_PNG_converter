import sys 
import os 
from PIL import Image

#grab the first and second argument
actual_route = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for filename in os.listdir(actual_route):
    img = Image.open(f'{actual_route}\{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_folder}\{clean_name}.png', 'png' )
    print('all done!')

        
        

# python3 converter ruta folder
#check if new exist, if not create it

#loop through champios

#convert images to png, can use pathlib

#save to the new folder