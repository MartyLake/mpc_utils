#!/usr/bin/python
import mpd
import sys
import io

if len(sys.argv) < 3 :
    print ("usage: {} [FILEOUT PATH] [URL] [PORT] [PASSWORD]".format(sys.argv[0]))
    print ("then, you can source this file in OBS studio in your BRB screen of Starting soon screen.")
    sys.exit(1)

FILEOUT=sys.argv[1]
URL=sys.argv[2]
PORT=sys.argv[3]
PASSWORD=None
if len(sys.argv) > 4:
    PASSWORD=sys.argv[4]

# use_unicode will enable the utf-8 mode for python2
# see https://python-mpd2.readthedocs.io/en/latest/topics/advanced.html#unicode-handling
client = mpd.MPDClient(use_unicode=True)
client.connect(URL, 6600)
if PASSWORD:
    client.password(PASSWORD)

while True:
    status = client.status()
    #for x in status:
    #    print(x, status[x])
    if not status["state"] == "play":
        print("Not playing.")
        with open(FILEOUT, "w") as f:
            f.write("Now playing: 4'33\" - John Cage")
    else:
        song = client.currentsong()
        #for x in song:
        #    print(x, song[x])
        outstr = "Now playing: {} - {}".format(song["title"], song["artist"])
        print(outstr)
        with io.open(FILEOUT, "w", encoding='utf-8') as f:
             f.write(outstr)

    client.idle()
