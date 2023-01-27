import av
import sys
import copy
import json

class SubtitlesReader:

    def __init__(self, args):
        self.args = args

    def get_subtitles(self):

        subs = []
        with av.open(self.args['media']) as container:

            for stream in container.streams:
                if stream.type == 'subtitle':
                    for packet in container.demux(stream):
                        subs.extend(packet.decode())
                    break
            else:
                print('No subtitle stream found')
                sys.exit(1)

        subset = subs[0]
        print(subset)

        for sub in subset[0]:
            print(sub)

        # Look for the first subtitle stream and dump all its packets
        #for stream in container.streams:
        #    if stream.type == 'subtitle':
        #        for packet in container.demux(stream):
        #            for frame in packet.decode():
        #                print(frame)
        #                for sub in frame:
        #                    print(sub)
        #        break
        #
        #else:
        #    print('No subtitle stream found')
        #    sys.exit(1)


        #for frame in container.decode(video=0):
        #    frame.to_image().save('frame-%04d.jpg' % frame.index)


        # media = Media(self.args.media)
        # # dump info
        # mediaInfo = media.info()

        # # select first subtitle stream
        # stStreams = [i for i, s in enumerate(mediaInfo['stream']) if s['type'] == 'subtitle']
        # if stStreams:
        #     stStream = stStreams[0]
        # else:
        #     print('No subtitle stream in %s' % mediaInfo['name'])
        #     sys.exit(2)

        # # dump subtitle header
        # print('header:')
        # print(mediaInfo['stream'][stStream]['subtitleHeader'])

        # count = 0
        # # iterate over media and decode subtitle packet
        # for pkt in media:
        #     if pkt.streamIndex() == stStream:

        #         # test only
        #         if self.args.copyPacket:
        #             pkt2 = copy.copy(pkt)
        #         else:
        #             pkt2 = pkt

        #         pkt2.decode()
        #         if pkt2.decoded:

        #             for i in range(pkt2.subtitle.num_rects):

        #                 if pkt2.subtitleTypes[i] == 'text':
        #                     print(pkt2.subtitle.rects[i].contents.text)
        #                 elif pkt2.subtitleTypes[i] == 'ass':
        #                     print(pkt2.subtitle.rects[i].contents.ass)
        #                 else:
        #                     print('non text subtitle...')

        #             count += 1
        #             if count != -1 and count > self.args.count:
        #                 break