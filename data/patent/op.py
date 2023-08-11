import codecs
import json
with codecs.open("./train/train.txt", "w", "utf-8") as fw_train, codecs.open("./valid/valid.txt", "w", "utf-8") as fw_valid:
    with codecs.open("/home/zhangkaiming/projects/patent_citation/data/spider_result.json", "r", "utf-8") as fr:
        count = 0
        for line in fr:
            jsonData = json.loads(line.strip())
            if count < 50000:
                if jsonData.get("标题"):
                    fw_train.write(jsonData.get("标题"))
                if jsonData.get("摘要"):
                    fw_train.write(jsonData.get("摘要"))
                if jsonData.get("说明书"):
                    fw_train.write(jsonData.get("说明书"))
                if jsonData.get("权利要求书"):
                    fw_train.write(jsonData.get("权利要求书"))
            elif 50000 <= count < 50500:
                if jsonData.get("标题"):
                    fw_valid.write(jsonData.get("标题"))
                if jsonData.get("摘要"):
                    fw_valid.write(jsonData.get("摘要"))
                if jsonData.get("说明书"):
                    fw_valid.write(jsonData.get("说明书"))
                if jsonData.get("权利要求书"):
                    fw_valid.write(jsonData.get("权利要求书"))
            else:
                break
            count += 1

