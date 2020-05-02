from pulsectl import Pulse, PulseVolumeInfo

def mute_spotify(mute_val: bool):
    with Pulse('Spotify-Mute') as pulse:
        # get a list of pulse-audio input sinks that contain "Spotify"
        spotify_sinks = [sink for sink in pulse.sink_input_list() if 'Spotify' in sink.name]
        for sink in spotify_sinks:
            # mute each instance of Spotify
            pulse.sink_input_mute(sink.index, mute = mute_val)
