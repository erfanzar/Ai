from __init import *


BottomSide = cv.imread(f'{Es}/BottomSide.jpg')
TopSide = cv.imread(f'{Es}/TopSide.jpg')
LeftSide= cv.imread(f'{Es}/LeftSide.jpg')
RightSide = cv.imread(f'{Es}/RightSide.jpg')



BottomSide = cv.resize(BottomSide,(150,150))
TopSide = cv.resize(TopSide,(150,150))
LeftSide = cv.resize(LeftSide,(150,150))
RightSide = cv.resize(RightSide,(150,150))



LeftArrow =  cv.imread(f'{Es}/LeftArrow.jpg',  )
RightArrow = cv.imread(f'{Es}/RightArrow.jpg', )
TopArrow =   cv.imread(f'{Es}/TopArrow.jpg',   )
BottomArrow= cv.imread(f'{Es}/BottomArrow.jpg',)

LeftArrow   = cv.resize(LeftArrow,  (150,150))
RightArrow  = cv.resize(RightArrow, (150,150))
TopArrow    = cv.resize(TopArrow,   (150,150))
BottomArrow = cv.resize(BottomArrow,(150,150))

# CalLeftArrow = (1-LeftArrow[:,:,3:] / 255) + \
#     LeftArrow[:,:,:3] * (LeftArrow[:,:,3:] / 255)


# CalRightArrow = (1-RightArrow[:,:,3:] / 255) + \
#     RightArrow[:,:,:3] * (RightArrow[:,:,3:] / 255)


# CalTopArrow = (1-TopSide[:,:,3:] / 255) + \
#     TopArrow[:,:,:3] * (TopArrow[:,:,3:] / 255)


# CalBottomArrow = (1-BottomArrow[:,:,3:] / 255) + \
#     BottomArrow[:,:,:3] * (BottomArrow[:,:,3:] / 255)
