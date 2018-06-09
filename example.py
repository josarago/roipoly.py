import logging

import numpy as np
from matplotlib import pyplot as plt
from roipoly import Roipoly


logger = logging.getLogger(__name__)

logging.basicConfig(format='%(levelname)s ''%(processName)-10s : %(asctime)s %(module)'
                            's.%(funcName)s:%(lineno)s %(message)s',
                    level=logging.DEBUG)

# create image
img = np.ones((100, 100)) * range(0, 100)

# show the image
plt.imshow(img, interpolation='nearest', cmap="Greys")
plt.colorbar()
plt.title("left click: line segment         right click: close region")

# let user draw first ROI
ROI1 = Roipoly(roicolor='r') #let user draw first ROI

# show the image with the first ROI
plt.imshow(img, interpolation='nearest', cmap="Greys")
plt.colorbar()
ROI1.display_roi()
plt.title('draw second ROI')

# let user draw second ROI
ROI2 = Roipoly(roicolor='b') #let user draw ROI

# show the image with both ROIs and their mean values
plt.imshow(img, interpolation='nearest', cmap="Greys")
plt.colorbar()
[x.display_roi() for x in [ROI1, ROI2]]
[x.display_mean(img) for x in [ROI1, ROI2]]
plt.title('The two ROIs')
plt.show()

# show ROI masks
plt.imshow(ROI1.get_mask(img) + ROI2.get_mask(img),
          interpolation='nearest', cmap="Greys")
plt.title('ROI masks of the two ROIs')
plt.show()


