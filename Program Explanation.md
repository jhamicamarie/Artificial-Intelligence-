#Program Explanation
# Warm vs Cool Color Classifier  
Supervised Machine Learning Project

This project is a Python program that predicts whether a color is classified as warm or cool based on its RGB values.  
It uses a small custom dataset containing primary, secondary, and tertiary colors and applies a Decision Tree Classifier to learn how color temperature relates to RGB values.

---

## Overview

This project demonstrates supervised machine learning. In supervised learning:

- Data contains labeled examples (warm or cool)
- The model learns by studying these examples
- The model can classify new, unseen inputs

Warm colors typically include reds, oranges, and yellows.  
Cool colors typically include blues, greens, and purples.

The goal of this project is to show how a machine learning model can make predictions based on patterns in RGB color data.

---

## Dataset (colors_dataset.csv)

The `colors_dataset.csv` file includes the following fields:

- `name` – English color name  
- `R`, `G`, `B` – RGB values of the color  
- `label` – target classification (warm or cool)

Available colors:
- red
- blue
- yellow
- orange
- green
- purple
- red-orange
- yellow-orange
- yellow-green
- blue-green
- blue-purple
- red-purple
