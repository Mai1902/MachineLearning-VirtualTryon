# Project Report

## Mai Nguyen Dac & Adam Shinomiya

## Project Summary

In the past two years, online shopping has became one of the essential parts of human's life since in person shopping might, ironically, expose costumers to the lethal virus. However, the instant blooming of E-commerce has a lot of problems, as past studies have asserted that customers perceive more risk with online or mobile shopping than offline purchasing (Schröder & Zaharia, 2008). Especially with Makeups and Personal care items, which was ranked as the number one items being bought online over the course of this pandemic, it is extremely hard for costumer to get the right products in this category due to the high level of diversity in skin tone, natural pigmentations, natural hair types, hormonal's needs, etc.. With what being said, our team suppose that a Virtual Product's Try-on should be a resolution for this complication since it will not only reduce the stress of costumer on finding their best fit, but also help firms on selling more products.

After a thorough research online and a review of materials covered in the class, we decided to create a Virtual Lipstick Try-on Application using opencv, numpy, and dlib. This application provides 6 different lipstick colors, including Punch, Rose, Brick red, Dusty rose, Nude, Royal blue which costumer can try them on virtually to see which color will look best on them. Once the color is decided, the machine will return with a range of recommended lipsticks that are sharing the same color code to the chosen color. By this way, clients will be able to get the right shade for their lipstick effortlessly, which will then save a lot of time and money for the clients. Moreover, this applications can help costumers to choose the suitable lipstick for other people as well, so having a gift as lipstick will not be a pain anymore.

## Usage guidelines

1. Downloading dependencies

- Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

- Upgrade pip if needed: `pip3 install --upgrade pip`

- Install dlib's dependencies with a list of command:
```
brew install cmake
brew install boost
brew install boost-python
brew install dlib
pip3 install numpy
pip3 install scipy
pip3 install scikit-image
```
- Install dlib: `pip3 install dlib` or `python3 -m pip install dlib`

- Install opencv: `pip3 install opencv-python`

2. Run command

The whole virtual try-on application run with command: `python3 lipstick_apply.py`

3. Try-on Image path guideline

- The command prompt will ask user for the file path that contain the image they want to try lipstick color on. User has to make sure that the file path is valid and thorough enough, for example: `/Users/Desktop/test_image_2.jpg`.

## Resources and references

[1] [Virtual Makeup using OpenCV source code](https://github.com/srivatsan-ramesh/Virtual-Makeup)

[2] [Lipstick Simulation Technique](https://static1.squarespace.com/static/5c3f69e1cc8fedbc039ea739/t/5d01686862182d0001b776a2/1560373362585/12_Lipstick_Simulation_Paper_For_Submission.pdf)

[3] [Another Virtual Make up source code](https://github.com/hriddhidey/visage)

[4] [The impact of AR on makeup firms](https://www.sciencedirect.com/science/article/pii/S0148296321002939)

## Experimental Results

1. Experiment with open/close mouth

This experiment is to test if the landmark coordinate can capture the entire lip when the mouth state is close and when the mouth state is open or showing a big smile.


| Mouth state      |   Original image   | Image after lipstick try on|
| ---------------- | ------------------- |---------------------------|
| Close mouth| ![1](experiment_image/original/closelip_whitelady_original.png)| ![1.1](experiment_image/colored_lip/closelip_whitelady_lipcolored.png)|
| Open mouth/big smile| ![2.1](experiment_image/original/openlip_asianlady_original.png)| ![2.2](experiment_image/colored_lip/openlip_asianlady_lipcolored.png) |

From the output, we can say that the landmark coordinate can successfully capture the whole lip even when the picture showing a big smile.

2. Experiment with different skin tones

This experiment is to test if the coloring method and parameters in color blending method still return a natural colored blended image with different skin tone.

| Skin tone      |   Original image   | Image after lipstick try on|
| ---------------- | ------------------- |---------------------------|
| Pale| ![](experiment_image/original/closelip_whitelady_original.png)|![](experiment_image/colored_lip/closelip_whitelady_lipcolored.png)|
| Fair|![](experiment_image/original/closelip_asianlady_original.png)|![](experiment_image/colored_lip/closelip_asianlady_lipcolored.png) |
| Dark|![](experiment_image/original/openlip_blacklady_original.png)|![](experiment_image/colored_lip/openlip_blacklady_lipcolored.png) |

From the experiment output, we see that the coloring method and parameters in color blending method always return a smoothed, well blended lip color with any user's skin tone.
