Commands to be issued:
=======================
 (C) 2018 Shayantan , Prateek 

source ~/.profile 
workon cv
cd /home/pi/Deep_Learning/object-detection-deep-learning
sudo modprobe bcm2835-v4l2

First capture image ( always stores as example_01.jpg ) using

  python capture.py



python deep_learning_object_detection.py \
	--prototxt MobileNetSSD_deploy.prototxt.txt \
	--model MobileNetSSD_deploy.caffemodel --image images/example_01.jpg 