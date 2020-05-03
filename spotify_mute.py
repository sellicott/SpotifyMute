#!/usr/bin/env python
from SwSpotify import spotify, SpotifyPaused, SpotifyClosed, SpotifyNotRunning
from threading import Thread
from sys import exit, platform
from time import sleep

from SpotifyCrossMute import mute_spotify 

if platform == "win32":
    # Windows
    from comtypes import CoInitialize


def main():

    t = Thread(target = worker, daemon=True)
    t.start()

    # main loop to detect user input
    while True:
        try:
            input()
        except EOFError:
            exit(0)
        except KeyboardInterrupt:
            exit(0)
    
def worker():
    song_name = ""
    prev_song_name = ""
    error_printed = False

    # if using windows initilize COM for this thread
    if platform == "win32":
        CoInitialize()

    while True:
        # sleep for a while
        sleep(0.5)
        try:
            song_name = spotify.song()
            error_printed = False
            error_msg = ""
        except SpotifyPaused:
            error_msg = "Spotify Paused"
        except SpotifyClosed:
            error_msg = "Spotify Closed"
        except SpotifyNotRunning:
            error_msg = "Spotify Not Running"

        if error_msg != "" and not error_printed:
            print(error_msg)
            error_printed = True 

        if song_name != prev_song_name:
            prev_song_name = song_name
            print(song_name)
            if 'Advertisement' in song_name or 'Spotify' in song_name:
                mute_spotify(True)
                print('Spotify Muted')
            else:
                mute_spotify(False)
                print('Spotify Unmuted')


if __name__ == "__main__":
    main()
