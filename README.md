# PRINTX

## Project Overview

This project aims to identify defective items on a processing line and remove them using a machine pusher. The core of this project is a vision model developed using Azure Custom Vision's object detection model. The model is deployed on a Jetson Nano developer board, and the output from the Jetson Nano GPIO pin is used to control the machine pusher and remove the defective item from the production line.

The system uses multiple IP cameras to capture video streams of the production line. These video streams are processed in real-time using NVIDIA DeepStream. When a defective item is detected, the system triggers the Jetson Nano's GPIO pin to activate the machine pusher. A monitoring system on the Jetson Nano keeps track of the detected defects.

## Getting Started


https://github.com/user-attachments/assets/97788ccf-8d09-44f2-a5e3-ce049c8de1ae






### Prerequisites

- Jetson Nano Developer Kit
- Multiple IP cameras
- Azure account with access to Custom Vision
- Docker installed on the Jetson Nano
- NVIDIA DeepStream SDK


![image](https://github.com/user-attachments/assets/a210b583-454e-4ef5-9ea5-7498455721bb)



### Installation

1. Set up your Jetson Nano Developer Kit and ensure Docker is installed.
2. Install the NVIDIA DeepStream SDK on the Jetson Nano.
3. Set up your IP cameras and ensure they are connected to the Jetson Nano.
4. Train your object detection model on Azure Custom Vision.
5. Export the model and download the Dockerfile.
6. Load the Dockerfile onto your Jetson Nano.

## Usage

Run the Dockerfile. The application will start processing video streams from the IP cameras, identify any defective items, and trigger the GPIO pin to activate the machine pusher and remove the defective item. The monitoring system on the Jetson Nano will keep track of the detected defects.

## Contributing

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request

## Resources:
Jetson GPIO python library: https://github.com/NVIDIA/jetson-gpio
combined with the DeepStream SDK python bindings (for running your model and calling out to Jetson GPIO: https://github.com/NVIDIA-AI-IOT/deepstream_python_apps.git

Azure Custom Vision : https://azure.microsoft.com/en-us/products/ai-services/ai-custom-vision

## Presentation for Demo Day
https://stdntpartners-my.sharepoint.com/:p:/g/personal/shakthi_lakmal_studentambassadors_com/Ec5RKjCSiURMqYaywyYSSrMBmdXTkMTwPP1k6TWH_eVL5Q?e=ArHD9z

## Contact

SHAKTHI LAKMAL - SHATHI.LAKMAL@studentambassadors.com
