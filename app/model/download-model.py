#Файл для установки нейронной модели к себе в репозиторий. Установится по этому пути app/model/save-model/tinkoff

if __name__ == '__main__':
    from transformers import AutoTokenizer, AutoModelWithLMHead

    mname = 'tinkoff-ai/ruDialoGPT-medium'
    
    tokenizer = AutoTokenizer.from_pretrained(mname)
    model = AutoModelWithLMHead.from_pretrained(mname)
    tokenizer.save_pretrained('app/model/save-model/tinkoff')
    model.save_pretrained('app/model/save-model/tinkoff')