## Canine Classifier App

# Introduction:
Provide an overview of the frontend repository's purpose and functionality.
Describe the technologies used, such as frontend frameworks, libraries, and UI components.

# Installation:
Include step-by-step instructions for setting up the frontend development environment.
List any dependencies and versions required.

# Usage:
Open the app using URL here: ![app](https://canine-classifier.streamlit.app/)
or using [QR code](https://github.com/wilsoncooked/canine-classifier-app/blob/master/images/qrcode.png)
How to use the app:
Step 1: Either take a photo using camera or upload an image from your device
Step 2: Adjust the square frame around the dog in the image
Step 3: Click 'Identify dog'
Step 4: You get a result of your dog's breeds information
Step 5 (optional): Try another dog's image by clicking on 'Try another dog' option

# UI Components:
Provide examples and usage guidelines for each component.
"Browse files" is for uploading the image of the dog. Any image in PNG, JPG, JPEG format upto 10 MB size can be uploaded. "Take Photo" can help to take live image of dog.
The output of dog's image classification are the example photo, general information about the breeds and the percentage of probabilities. Top 5 classes of breeds are listed and the rest are cumulated as 'Others'. If percentage in 'Others' is larger than 75, then results shows "It doesn't look like a dog!".
Next to these results, there is an original image which was uploaded and also a gradcam image as to show how computer visualizes the dog.
If users want to try another image, it can be done by clicking 'Try another dog'.

# Routing:
Document the application routes and their corresponding components/pages.

# Reporting issues:
We are happy to address the issues raised. Please report it in the issues section of GitHub.

# License:
GNU General Public License (GPL) v3
    Copyright (C) 2024 Sarah Wilsoncook, Marcel Lommerzheim, Pessi Virta, Jaydeep Bhat

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


Run Streamlit web server:
```bash
make streamlit
```
