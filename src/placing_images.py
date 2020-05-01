from PIL import Image, ImageFont, ImageDraw
from math import sin, cos, pi
import os

def get_all_positions(draw, centre, angle, lenght):
  listofpos = []
  for start in range(0, 360,int(angle)):
      end = (start+angle) * pi/180
      start *= pi/180
      position = int(centre[0] + lenght*cos(start)), int(centre[1] + lenght*sin(start))
      listofpos.append(position)

  return listofpos

def generate_image_from_list(list_of_card):
    images_list = []

    for image in os.listdir("./images/"):
        if image[-3:] == 'png':
            images_list.append("./images/"+image)
        elif image[-3:] == 'gif':
            images_list.append("./images/"+image)
        elif image[-3:] == 'jpg':
            images_list.append("./images/"+image)
        elif image[-4:] == 'jpeg':
            images_list.append("./images/"+image)
        elif image[-3:] == 'BMP':
            images_list.append("./images/"+image)
        elif image[-4:] == 'TIFF':
            images_list.append("./images/"+image)
        else:
            pass

    try:
        inc1 = 0
        for card in list_of_card:
            resolution = (100,100)
            split_360 = 360 / len(card)

            background_image = Image.open('./background/circle.png')
            draw = ImageDraw.Draw(background_image)
            data = get_all_positions(draw, (250, 250), split_360, 200)

            inc = 0
            for img in card:
                im = Image.open(images_list[img]).resize(resolution)
                background_image.paste(im, data[inc])
                inc = inc + 1

            inc1 = inc1 + 1
            background_image.save("./generate/card_"+str(inc1)+".png")
            print("[ * ] New Card Generated : /generate/card_"+str(inc1)+".png")

    except KeyboardInterrupt:
        print('\n[ * ] CTRL + C')

    except:
        print('\n[ * ] Insufficient Number Of Images')

    print()
