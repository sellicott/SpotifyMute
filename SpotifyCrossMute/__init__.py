"""
This module implements a single function mute_spotify which (self descriptively) mutes
Spotify. It should work on Windows, Mac and Linux (tested on Windows 10, and Arch Linux).
"""

name = 'SpotifyCrossMute'
__version__ = '1.0.0'

from sys import platform

def mute_spotify(mute_val: bool):
    '''
    Finds spotify application and mutes or unmutes it based on the value of mute_val.
    The input argument to the function sets the mute state of Spotify. The value
    is True for muted False for unmuted.
    Returns: nothing.
    '''

    if platform == 'linux' or platform == 'linux2':
        _mute_spotify_linux(mute_val)
    elif platform == 'darwin':
        pass
    elif platform == 'win32':
        _mute_spotify_win32(mute_val)

def _mute_spotify_linux(mute_val: bool):
    from pulsectl import Pulse, PulseVolumeInfo
    with Pulse('Spotify-Mute') as pulse:
        # get a list of pulse-audio input sinks that contain "Spotify"
        spotify_sinks = [sink for sink in pulse.sink_input_list() if 'Spotify' in sink.name]
        for sink in spotify_sinks:
            # mute each instance of Spotify
            pulse.sink_input_mute(sink.index, mute = mute_val)

def _mute_spotify_win32(mute_val: bool):
    from pycaw.pycaw import AudioUtilities
    sessions = AudioUtilities.GetAllSessions()
    mute_int = 0
    if mute_val:
        mute_int = 1
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Spotify.exe":
            volume.SetMute(mute_int, None)

__all__ = [mute_spotify]
