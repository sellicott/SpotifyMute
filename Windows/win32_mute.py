from pycaw.pycaw import AudioUtilities


def mute_spotify(mute_val: bool):
    sessions = AudioUtilities.GetAllSessions()
    mute_int = 0
    if mute_val:
        mute_int = 1
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Spotify.exe":
            volume.SetMute(mute_int, None)
