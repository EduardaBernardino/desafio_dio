import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from image_processing.utils import io, plot
from image_processing.processing import combination, transformation


image1 = io.read_image("C:/Users/eduar/OneDrive/TI/desafio-dio/logo.png/logo")
image2 = io.read_image("C:/Users/eduar/OneDrive/TI/desafio-dio/oculos.webp/oculos")


plot.plot_image(image1)
plot.plot_image(image2)



result_image = combination.tranfer_histogram(image1, image2)
plot.plot_result(image1, image2, result_image)