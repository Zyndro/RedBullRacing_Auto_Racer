# Semi automated RedBull Racing script
Made for https://www.redbull.com/pl-pl/projects/red-bull-racers-polska-2022

This script detects the race start and then executes the predefined input.

# Requirements
  * This script will run only under Windows
  * Python 3.10

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip3 install -r requirements.txt
```

## Usage
First time run:

* Start the race, then start this script: ```StartLightPosition.py```
* alt tab to the game window and click in the middle of the start lights to get their position.
* Edit the ```StartRace.py``` with values you got from the first script, lines 7-8
    ```
    start_light_x = 
    start_light_y = 
    ```
* Start the race and run ```StartRace.py``` when the camera stops spinning(picture below), keep focus on the browser window

  ![obraz](https://user-images.githubusercontent.com/45998308/193125170-843f06dd-c826-41d0-8531-1559b3d44fdf.png)



You can tweak the inputs in the ```race_start``` function in ```StartRace.py``` file.