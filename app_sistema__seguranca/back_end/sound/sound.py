from pydub import AudioSegment
from pydub.playback import play

def play_alert(sound_file):
    alert_sound = AudioSegment.from_file(sound_file)
    play(alert_sound)