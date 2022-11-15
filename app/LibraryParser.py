'''
The playlist file has format 
#EXTINF:404,Dualism, Meeloo - I Beg You
E:\Contents\Dualism, Meeloo\Progressive & Psy Trance Pieces Vol.4\I Beg You.mp3
'''

songs = {}
word_list = {}
ignore=['the','of','in','to','a','on','for','feat.','are','&','ey','remix']

#read the file

with open("trance.m3u8", encoding="utf-8") as f:
    #just take the lines with # in front 
    # and not the same number after the :
    # and filter out the ones with psy in their path
    for line in f:
        if line[0] != '#':
            continue

        a = line.split(':')
        if len(a) < 2:
            continue

        #the title of the song is after the first -
        split_line = line.strip('#EXTINF:').split('-')
        song_num = split_line[0].split(',')[0] #this takes the number in front
        artist = split_line[0].strip(song_num+',').strip()
        title = split_line[1].split('(')[0].strip()
        if len(split_line) > 2:
            remix = split_line[2]

        #add the artist and song if they're not already in the list     
        if artist in songs:
            if title in songs[artist]:
                continue
            else:
                songs[artist].append(title)
        else:
            songs[artist] = [title]

# now go through all the songs and add up all the words
for artist in songs.items():
    for song in artist[1]:
        words = song.lower().split(' ')
        for word in words:
            if len(word) == 0:
                continue
            # try to account for plurals
            w = word
            if w[-1]== 's':
                if len(w[:-2]) == 0:
                    continue
                w = w[0:-2]
            if w in word_list:
                word_list[w] += 1
            else:
                word_list[w] = 1

#sort the dictionary
sorted_words = {k: v for k, v in sorted(word_list.items(), key=lambda item: item[1])}
for i in sorted_words.items():
    print(i)
print(sorted_words["star"])
