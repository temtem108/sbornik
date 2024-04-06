import json
def get_articles():
    with open("articles.json", "r", encoding="utf-8") as f:
        try:
            file = json.load(f)
        except:
            print("Файл не найден.")
            file = {}

        return file 


def save_article(name, text):
    with open("articles.json", "r", encoding="utf-8") as f:
       file  = json.load(f)
       file [name] = text
    with open("articles.json", "w", encoding="utf-8")as f:
        json.dump(file, f, ensure_ascii=False) 
        

def delete_article(name):
    with open("articles.json", "r", encoding="utf-8") as f:
       file  = json.load(f)
       del file [name] 
    with open("articles.json", "w", encoding="utf-8")as f:
        json.dump(file, f, ensure_ascii=False)         