# Semi automated RedBull Racing script
Made for https://www.redbull.com/pl-pl/projects/red-bull-racers-polska-2022

This script detects the race start and then executes the predefined input.

# Requirements
  * Python 3.10

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip3 install -r requirements.txt
```

## Usage
First time run:

* Start the game, then start this script: ```StartLightPosition.py```
* alt tab to the game window and click in the middle of the start lights when they are gray and again when they are red(click in the same spot)
* Edit the ```StartRace.py``` with values you got from the first script, lines 7-10
    ```
    start_light_x = 
    start_light_y = 
    gray = 
    red = 
    ```
* Run ```StartRace.py``` and start the race(keep window focus on the game).

You can tweak the inputs in the ```race_start``` function in ```StartRace.py``` file.