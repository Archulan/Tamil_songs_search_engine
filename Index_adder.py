import codecs
import json
import random

f = codecs.open('160040D_lyrics_output.txt', 'w', encoding='utf-8')

json_file = open("160040D_tamil_songs_corpus_1.txt", encoding='utf-8', errors='ignore')

i=1
for line in json_file:
    try:
        print(i)
        song_json = json.loads(line)
        print(song_json)
        del song_json['movie_url']
        del song_json['song_url']
        del song_json['movie_image']
        song_json["மதிப்பீடு"] = random.randint(1, 5)

        f.write('{ "index" : { "_index" : "songs_db", "_type" : "songs", "_id" :' + str(i) + ' } }\n')
        json.dump(song_json, f, ensure_ascii=False)
        f.write('\n')
        i += 1
        # print(song_json)
        print()

        # f.write(str(song_json)+'\n')
    except Exception as e:
        print(e)
