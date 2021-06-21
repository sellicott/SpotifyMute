# SpotifyMute
A cross platform python script for muting Spotify while it is playing an ad. Based on 
SwSpotify which gets the current track from Spotify. The application uses the operating
system to mute the Spotify application. This is Pulse Audio for Linux, the Windows 
SimpleAudio API, and applescript for Mac.

# Useage
The script watches Spotify notifications to see what current song is playing, if it detects an
ad, it will mute Spotify. To run the program execute:
```
python spotify_mute.py
```
in the directory where the script is located.

The script will show the currently playing song, and tell if it has muted Spotify or not. It 
will also display a message if Spotify is paused or closed.

On windows I highly recommend running the script in PowerShell over command prompt (`cmd`) 
or Git Bash. When running with Git Bash, the script seems to miss adds significantly more often.

# Installation
This script requires Python 3, you have to install that first.
All platforms need SwSpotify, install it with
```
pip install SwSpotify
```
## Linux
Linux needs a Python library to hook into Pulse Audio
```
pip install pulsectl
```
## Windows
Windows need a Python library to control the Windows audio system, and another for interfacing
with COM objects
```
pip install pycaw comtypes
```
## Mac
I am not really sure yet
