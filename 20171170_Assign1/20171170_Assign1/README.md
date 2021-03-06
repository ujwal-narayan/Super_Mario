# Python Super Mario Game 
========================================================<br/>
By Ujwal Narayan

## Motivation 

A terminal based implementation that tries to simulate the classic Super Mario<br/>
Written in python3 without using pygame and curses.<br/>
Only *colorama* and *numpy* has been used to bring in colours.<br/>
The game has been tested only on Linux based operating systems, may not work on Windows.

### Prerequisites

- First, install all the requirements
	- `pip install -r requirements.txt`
- Running the game using python3
	- `python3 game.py`
- Runs on Unix Machines . Modify the input.py by uncommenting the ones out for Windows machines.

### GamePlay

  Normal Mario game . Bricks are not breakable .Cyan objects a powerup which will let you run down an enemy without respawning <br/>

  Higher levels have :
  - Pits
  - Smarter Enemy movement 
  - Faster enemy movement
  

##### Controls
 You can move mario around using the following controls(make sure *CAPS_LOCK* is off):
 - `d`  to move right
 - `a`  to move left
 - `w`  or `Space_bar` key to jump . Press it twice to Double Jump 
 - `q` to quit the game
 

 Mario can collect coins and power ups which add to the score <br/>

 Mario can kill enemies by jumping over them.Dead Enemies add to your score . Enemies kill you if you hit them  from the side ,If you die but have lives left  you need to restart the level.You Fall inside the pit , game over  <br/>

 A score is generated according to the maximum distance traveled in the game.<br/>

 Game is over when you run out of lives . 

 
### Code Structure

The game has been written keeping in mind OOP principles.<br/>
The application demonstrates inheritance, encapsulation and polymorphism.<br/>
The code is modular and documneted . 
It is also pep8 compliant 


## Changes made 

### Pylint Changes 

+ Changed variable names to pep8 conventions
+ Fixed Trailing whiespace 
+ Fixed the line length 
+ Fixed the invalid names 
+ Followed the proper name conventions for variables 
+ Fixed acess to protected class 

A few errors were locally disabled. One was too-few-public-class.While understandable that Classes must not be used to store data , often it is the best method to use for your needs as is the case here. Rather than adding few useless public methods which would only result in obsfucating the code , the errors were locally disabled.Another error that was disabled was the import error as you would have to configure the path for the pacakges in pylint correctly.`msvcrt` is needed only for windows and as it is not essential for unix systems it is not mentioned in the requirements. 

Pylint score : 9.06 
