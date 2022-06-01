import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow as disp # for image display

## AUTHORS ##

## TRABALHO FEITO COM O OBJETIVO
## DE IDENTIFICAR O NÍVEL DE POLUIÇÃO 
## LUMINOSA NA REGIÃO

# Gabriel Henrique Hoppe Coelho

def hasTopNeighbor(image, row, col):
    rows, cols, _  = image.shape

    if (row - 1 < 0): return False

    return True

def hasRightNeighbor(image, row, col):
    rows, cols, _ = image.shape

    if (col + 1 > (cols - 1)): return False

    return True

def hasBottomNeighBor(image, row, col):
    rows, cols, _ = image.shape

    if (row + 1 > (rows - 1)): return False

    return True

def hasLeftNeighBor(image, row, col):
    rows, cols, _ = image.shape

    if (col - 1 < 0): return False

    return True

def getPollutionLevel(imageName, image):
  
  print(imageName)
  disp(image)
  
  rows, cols, _ = image.shape

  x = 0

  for i in range(rows):
    for j in range(cols):
      x += getPixelPatternPercentage(image, i, j)

  x = x / (rows * cols)

  print(x)
  print("\n\n")

  return x

def comparePixels(p1, p2):
  allcolorsPattern = 0;

  p1r = p1[0]
  p1g = p1[1]
  p1b = p1[2]

  p2r = p2[0]
  p2g = p2[1]
  p2b = p2[2]

  if (p1r > p2r):
    allcolorsPattern += p2r / p1r
  else:
    allcolorsPattern += p1r / p2r

  if (p1g > p2g):
    allcolorsPattern += p2g / p1g
  else:
    allcolorsPattern += p1g / p2g

  if (p1b > p2b):
    allcolorsPattern += p2b / p1b
  else:
    allcolorsPattern += p1b / p2b

  allcolorsPatternPercentage = allcolorsPattern / 3

  return allcolorsPatternPercentage

def getPixelPatternPercentage(image, row, col):
    
    pixel = image[row, col]

    numberOfNeighbors = 0;
    patternMatching = 0;

    ## TOP ##
    if (hasTopNeighbor(image, row, col)):

      numberOfNeighbors += 1
      topPixel = image[row - 1, col]

      allcolorsPatternPercentage = comparePixels(pixel, topPixel)

      patternMatching += allcolorsPatternPercentage

    ## RIGHT ##
    if (hasRightNeighbor(image, row, col)):
      
      numberOfNeighbors += 1
      rightPixel = image[row, col + 1]

      allcolorsPatternPercentage = comparePixels(pixel, rightPixel)

      patternMatching += allcolorsPatternPercentage

    ## BOTTOM ##
    if (hasBottomNeighBor(image, row, col)):

      numberOfNeighbors += 1
      bottomPixel = image[row + 1, col]

      allcolorsPatternPercentage = comparePixels(pixel, bottomPixel)

      patternMatching += allcolorsPatternPercentage

    ## LEFT ##
    if (hasLeftNeighBor(image, row, col)):

      numberOfNeighbors += 1
      leftPixel = image[row, col - 1]

      allcolorsPatternPercentage = comparePixels(pixel, leftPixel)

      patternMatching += allcolorsPatternPercentage


    return patternMatching / numberOfNeighbors



grandes_cidades = cv.imread("/content/images/grandes_cidades.png");
ceu_urbano = cv.imread("/content/images/ceu_urbano.png");
ceu_sub_urbano = cv.imread("/content/images/ceu_sub_urbano.png");
rural_para_suburbano = cv.imread("/content/images/rural_para_suburbano.png");
ceu_rural = cv.imread("/content/images/ceu_rural.png");
ceu_esuro = cv.imread("/content/images/ceu_escuro.png");
ceu_esuro_excelente = cv.imread("/content/images/ceu_escuro_excelente.png");

getPollutionLevel("GRANDES CIDADES", grandes_cidades)
getPollutionLevel("CEU URBANO", ceu_urbano)
getPollutionLevel("CEU SUB URBANO", ceu_sub_urbano)
getPollutionLevel("RURAL PARA SUB URBANO", rural_para_suburbano)
getPollutionLevel("CEU RURAL", ceu_rural)
getPollutionLevel("CEU ESCURO", ceu_esuro)
getPollutionLevel("CEU ESCURO EXCELENTE", ceu_esuro_excelente)