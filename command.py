import os
from rembg import remove
from PIL import Image

def hitung():
    filedir = os.listdir("./input")
    return len(filedir)

def resize(brp):
    image = Image.open(f'./output/out_{brp}.png')
    img = image.resize((1080,1080))
    img.save(f'./output/pres_{brp}.png')

def watermark(brp):
    temp_image = Image.open('./bg.jpeg')
    watermark = Image.open(f'./output/pres_{brp}.png')    

    if watermark.mode!='RGBA':
        alpha = Image.new('L', watermark.size, 15)
        watermark.putalpha(alpha)

    paste_mask = watermark.split()[3].point(lambda i: i)
    temp_image.paste(watermark, (0,0), mask=paste_mask)
    temp_image.save(f'./prestige/prestige_{brp}.jpg')

def run_all(brp):
    filedir = os.listdir("./input")
    def rmv(direc,count):
        input_path = f'./input/{direc}'
        output_path = f'./output/out_{count+1}.png'

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,only_mask=False,post_process_mask= False)
                o.write(output)
        os.remove(input_path)
        
    loop=0
    while(loop<brp):
        rmv(filedir[loop],loop)
        loop=loop+1

def run_pres(brp):
    filedir = os.listdir("./input")
    def rmv(direc,count):
        input_path = f'./input/{direc}'
        output_path = f'./output/out_{count+1}.png'
            
        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,only_mask= False,post_process_mask= False)
                o.write(output)
        os.remove(input_path)
        
    loop=0
    while(loop<brp):
        rmv(filedir[loop],loop)
        resize(loop+1)
        watermark(loop+1)
        print(f"{loop+1} picture done!")
        loop=loop+1
