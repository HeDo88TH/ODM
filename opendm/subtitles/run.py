# Import the required modules
from opendm.subtitles import SubtitlesReader

params = {}
params.media = "/datasets/sample.mkv"
params.copyPacket = False

sr = SubtitlesReader(params)

sr.get_subtitles()