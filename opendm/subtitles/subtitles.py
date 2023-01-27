from avpy import Media
import sys
import copy

class SubtitlesReader:

    def __init__(self, args):
        self.args = args

    def get_subtitles(self):

        media = Media(self.args.media)
        # dump info
        mediaInfo = media.info()

        # select first subtitle stream
        stStreams = [i for i, s in enumerate(mediaInfo['stream']) if s['type'] == 'subtitle']
        if stStreams:
            stStream = stStreams[0]
        else:
            print('No subtitle stream in %s' % mediaInfo['name'])
            sys.exit(2)

        # dump subtitle header
        print('header:')
        print(mediaInfo['stream'][stStream]['subtitleHeader'])

        count = 0
        # iterate over media and decode subtitle packet
        for pkt in media:
            if pkt.streamIndex() == stStream:

                # test only
                if self.args.copyPacket:
                    pkt2 = copy.copy(pkt)
                else:
                    pkt2 = pkt

                pkt2.decode()
                if pkt2.decoded:

                    for i in range(pkt2.subtitle.num_rects):

                        if pkt2.subtitleTypes[i] == 'text':
                            print(pkt2.subtitle.rects[i].contents.text)
                        elif pkt2.subtitleTypes[i] == 'ass':
                            print(pkt2.subtitle.rects[i].contents.ass)
                        else:
                            print('non text subtitle...')

                    count += 1
                    if count != -1 and count > self.args.count:
                        break