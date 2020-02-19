import numpy as np
import cv2
from PIL import Image

im=cv2.VideoCapture(0)

#im.set(3,320)
#im.set(4,320) 

print("""
	///////////////////////////////////////
	|              PROGRAM                |
	|                                     |
	| Program przechwytuje obraz z kamery |
	| Aby zapisac jako zdjecie nacisnij s |
	| Aby wyjsc nie zapisujac nacisnij q  |
	|                                     |
	|                                     |
	///////////////////////////////////////
 
		                                     
		
"""
 )


while True:
	
	val,zdjecie = im.read()
	
	zdjecie[:,:,0]=0
	zdjecie[:,:,1]=0
	
	cv2.imshow('zdjecie',zdjecie)
	key = cv2.waitKey(1)
	
	if key == ord('q'):
		break
	elif key == ord('s'):
		nazwa = raw_input('Podaj nazwe zdjecia z koncowka formatu lub napisz d aby zrobic jeszcze jedno zdjecie NP: zdjecie.png : ')
		if nazwa == 'd':
			continue
		else:
			print 'zapisano zdjecie o nazwie : ', nazwa
			cv2.imwrite(nazwa,zdjecie)
			break
	
	

#zdjecie=cv2.imshow('106826.jpg',1)
#cv2.namedWindow('zdjecie', cv2.WINDOW_NORMAL)

#cv2.waitKey(0)
#cv2.imwrite('zdjecie.jpg',zdjecie)
im.release()
cv2.destroyAllWindows()
