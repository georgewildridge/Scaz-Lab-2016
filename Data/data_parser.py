import Image
import json

for i in range(8): #change
	if i < 10:
		im = Image.open('Mis/8/frame000' + str(i) + '.jpg') #change
	else:
		im = Image.open('Mis/8/frame00' + str(i) + '.jpg') #change
	im.save('Mis/boards/board_' + str(383 + i) + '.png') #change
	open('Mis/boards/board_' + str(383 + i) + '.json','w') #change


# for name in ['frame_000{}'.format(1 + i) for i in range(9)]:
#     print(name)
# 	im = Image.open(name + '.jpg')
# 	im.save(name + '.png')
