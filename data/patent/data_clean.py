import codecs
import re
'''
with codecs.open("train.txt", "w", "utf-8") as fw:
    with codecs.open("train_refine.txt", "r", "utf-8") as fr:
        for line in fr:
            line = line.strip(" ").strip(" ")
            if not line:
                continue
            line = re.sub("\[\d+\]", "", line)
            line = line[:5] + re.sub("\(\d+\)", "", line[5:])
            line = line[:5] + re.sub("（\d+\）", "", line[5:])
            line = line.strip()
            if line:
                fw.write(line + "\n")
'''
with codecs.open("1.txt", "w", "utf-8") as fw:
    with codecs.open("test.txt", "r", "utf-8") as fr:
        for line in fr:
            line = line.strip(" ").strip(" ")
            if not line:
                continue

            if line:
                fw.write(line + "\n")
