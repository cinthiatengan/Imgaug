# -*- coding: utf-8 -*-
"""ImageAugLib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QbHMLQskqoevLkrCQWXno6TUMuGi7GUm

1 - Load and Augment an Image  

*imgaug* expect images to be numpy arrays and works best with dtype **uint8** (0 to 255).
"""

pip install imgaug

pip install imagecorruptions

# Commented out IPython magic to ensure Python compatibility.
import imageio
import imgaug as ia
# %matplotlib inline

image = imageio.imread("https://i.imgur.com/CQX4aLU.png") #variavel para guardar e ler a imagem que desejamos utilizar.

print("Original: ")
ia.imshow(image)

"""2 - Augment the Image
using **Affine**
"""

from imgaug import augmenters as iaa
ia.seed(4)

rotate = iaa.Affine(rotate = (-25,25)) #criando uma variavel que utiliza o metodo affine para rodar a imagem, dentro daqueles parametros entre -25 e 25)
image_aug = rotate(image = image) # aqui guarda em uma nova variável essa rotação da imagem original.

print("Augmented: ")
ia.imshow(image_aug)

"""3 - Augment a Batch of Images"""

import numpy as np

images = [image, image, image, image] #guardamos a mesma imagem varias vezes num array
images_aug = rotate(images=images)    #pegamos o array e aplicamos o affine utilizado anteriormente para rotacionar aleatoriamente entre aquele intervalo

print("Augmented Batch: ")
ia.imshow(np.hstack(images_aug))

"""4 - Use many augmentation techniques simultaneously

use of Affine, GaussianNoise and crop
"""

seq = iaa.Sequential([
    iaa.Affine(rotate=(-25,25)),
    iaa.AdditiveGaussianNoise(scale=(10,60)),
    iaa.Crop(percent=(0,0.2))
])
images_aug = seq(images=images) #adiciona a sequencia de filtros as imagens do images_aug (array)

print("Augmented: ")
ia.imshow(np.hstack(images_aug))

seq = iaa.Sequential([
  iaa.Affine(rotate=(-25,25)),
  iaa.AdditiveGaussianNoise(scale=(30,90)),
  iaa.Crop(percent=(0,0.4))
], random_order=True) # adição de ordem aleatoria a adição de filtros as imagens

images_aug = [seq(image=image) for _ in range(8)]

print("Augmented: ")
ia.imshow(ia.draw_grid(images_aug, cols=4, rows=2))

"""5- Augmenting Images of different sizes"""

seq = iaa.Sequential([
  iaa.CropAndPad(percent=(-0.2,0.2), pad_mode="edge"),
  iaa.AddToHueAndSaturation((-60,60)),
  iaa.ElasticTransformation(alpha=90, sigma=9),
  #iaa.Cutout()
], random_order=True)

# Load images with different sizes
images_different_sizes = [
  imageio.imread("https://i.imgur.com/xifv6Tv.jpg"),
  imageio.imread("https://i.imgur.com/e89a9Lv.jpg"),
  imageio.imread("https://i.imgur.com/twKCU4z.jpg")
]

# Augment them as one batch
images_aug = seq(images=images_different_sizes)

# Visualize the results
print("Image 0")
ia.imshow(np.hstack([images_different_sizes[0], image_aug[0]]))

#print("Image 1 ")
#ia.imshow(np.hstack([images_different_sizes[1], image_aug[1]]))

#print("Image 2")
#ia.imshow(np.hstack([images_different_sizes[2], image_aug[2]]))

seq = iaa.Sequential([
    iaa.CropAndPad(percent=(-0.2, 0.2), pad_mode="edge"),  # crop and pad images
    iaa.AddToHueAndSaturation((-60, 60)),  # change their color
    iaa.ElasticTransformation(alpha=90, sigma=9),  # water-like effect
    #iaa.Cutout()  # replace one squared area within the image by a constant intensity value
], random_order=True)

# load images with different sizes
images_different_sizes = [
    imageio.imread("https://upload.wikimedia.org/wikipedia/commons/e/ed/BRACHYLAGUS_IDAHOENSIS.jpg"),
    imageio.imread("https://upload.wikimedia.org/wikipedia/commons/c/c9/Southern_swamp_rabbit_baby.jpg"),
    imageio.imread("https://upload.wikimedia.org/wikipedia/commons/9/9f/Lower_Keys_marsh_rabbit.jpg")
]

# augment them as one batch
images_aug = seq(images=images_different_sizes)

# visualize the results
print("Image 0 (input shape: %s, output shape: %s)" % (images_different_sizes[0].shape, images_aug[0].shape))
ia.imshow(np.hstack([images_different_sizes[0], images_aug[0]]))

print("Image 1 (input shape: %s, output shape: %s)" % (images_different_sizes[1].shape, images_aug[1].shape))
ia.imshow(np.hstack([images_different_sizes[1], images_aug[1]]))

print("Image 2 (input shape: %s, output shape: %s)" % (images_different_sizes[2].shape, images_aug[2].shape))
ia.imshow(np.hstack([images_different_sizes[2], images_aug[2]]))