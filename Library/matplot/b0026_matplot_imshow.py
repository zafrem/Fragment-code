import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

image = img.imread('./imshow.png')
# image array
# [[[0.9372549  0.9254902  0.89411765]
#   [0.91764706 0.92941177 0.89411765]
#   [0.9137255  0.93333334 0.8901961 ]
#   ...
plt.imshow(image, cmap='viridis')
plt.colorbar()
plt.title('Array to image')
plt.show()

# Color Gray
plt.imshow(image[:,:,[0,0,0]], cmap='viridis')
plt.colorbar()
plt.title('Array to image')
plt.show()

# Gray Channel
plt.imshow(image[:,:,0], cmap='gray')
plt.colorbar()
plt.title('Array to image')
plt.show()