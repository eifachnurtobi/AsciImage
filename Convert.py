import json
from argparse import ArgumentParser
try:
	from PIL import Image, ImageStat, ImageEnhance, ImageOps
except ImportError:
	print("Please install Python Pillow\n(Pip install Pillow)")
	quit()



def resizeImg(img, width):
	resHeight=int(img.size[1]/(img.size[0]/width))
	RoundedHeight=resHeight-(resHeight%20)
	try:
		return img.resize((width,resHeight), Image.ANTIALIAS)
	except ValueError:
		print("Image too small. Please try a different one")
		quit()


def PrintImg(ResImg):	
	for y in range(0, ResImg.size[1]-9, 20):
		for x in range(0, ResImg.size[0], 9):
			ColorVal = (ImageStat.Stat(ResImg.crop((x,y,x+9,y+20))).mean)[0]
			for i in OrderedKeys:
				if float(i) > ColorVal:
					CorrIndex = str(OrderedKeys[(OrderedKeys.index(i)-1)])
					Character = chr(int(Characters[CorrIndex]))
					print(Character, end="")
					break
				else:
					continue
		print("\n", end="")

parser = ArgumentParser(description="Turn images into ASCII.")
parser.add_argument("-f", dest="filename",help="Input file")
parser.add_argument("-w", dest="width", type=int, help="Width of the final ASCII image in letters (Default is 100)", default=100)
parser.add_argument("-c", dest="contrast",type=float, help="Adds additional contrast to the image, default is 1.0 (higher = more contrast)", default=1.0)
parser.add_argument("-ea", dest="extendedRange",action="store_true", help="Add switch to use extended ASCII range (Yes i know technically 'extended ASCII' is wrong)")
parser.add_argument("-i", dest="invert",action="store_true", help="Inverts the image before converting")
parser.add_argument("-b", dest="blocked",nargs='+', help="Blocks certain specified characters from appearing in Ascii art image", default=[])
args = parser.parse_args()

OrigImg = Image.open(args.filename).convert("RGB")
if(args.invert):
	OrigImg = ImageOps.invert(OrigImg)
AdjustedContrast = ImageEnhance.Contrast(OrigImg).enhance(args.contrast)
Processed = AdjustedContrast.convert("LA")
#Use extended range if is specified
if(args.extendedRange):
	Characters = json.load(open("ExtendedCharacters.json"))
else:
	Characters = json.load(open("Characters.json"))
#Filter out blocked Characters

for n,v in enumerate(args.blocked):
	if type(v) is str or unicode:
		args.blocked[n] = str(ord(v))

torem=[]
for key in list(Characters):
	for char in args.blocked:
		if(Characters[key] == char): 
				torem.append(key)

for key in torem:
	del Characters[key]

OrderedKeys = sorted(Characters.keys(), key=float)
ResImg = resizeImg(Processed, int(args.width)*9)
PrintImg(ResImg)


