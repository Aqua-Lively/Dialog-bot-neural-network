import torch
from transformers import AutoTokenizer, AutoModelWithLMHead


# Класс блягодаря которому, происходит взаимодействие телеграмм бота с нейронной сеть.


class NeiroDialogBot:

    def __init__(self,model):
        self.tokenizer = AutoTokenizer.from_pretrained('app/model/save-model/tinkoff')
        self.model = AutoModelWithLMHead.from_pretrained('app/model/save-model/tinkoff')
        self.chat = ''

    def replyToTheMessage(self, message: str) -> str:
        """
        На вход поступает сообщение от собесдника. В дальнейшем идёт обработка сообщений у нейронной сети, потом полученные данные от нейронной сети
        обрабатываются и обратно отправляются телеграм боту.
        """
        
        self.chat += f'@@ПЕРВЫЙ@@{message}@@ВТОРОЙ@@'
        inputs = self.tokenizer(f'{self.chat}', return_tensors='pt')
        generated_token_ids = self.model.generate(
            **inputs,
            top_k=10,
            top_p=0.95,
            num_beams=3,
            num_return_sequences=1,
            do_sample=True,
            no_repeat_ngram_size=2,
            temperature=1.2,
            repetition_penalty=1.2,
            length_penalty=1.0,
            eos_token_id=50257,
            max_new_tokens=40
        )
        context_with_response = [self.tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
        context_with_response = self.clearContext(context_with_response[0],self.findLastIdMessage(context_with_response[0]))
        self.chat += context_with_response


        print('##########################################')
        print(self.chat)
        print('##########################################')

        return context_with_response

    def clearContext(self, context: str, id: int) -> str:
        """
        На вход идут два параментра. Первый это контекст, который отдала нейронка и который нужно подать собеседнику в правильном виде. А второй параметр - это index(id) места с которого начинается  работа со строкой, чтобы забрать из неё только нужное. На выходе строка.
        """
        string = ''
        id+=1
        while id < len(context) and context[id] != '@':
            string+= context[id]
            id+=1
        return string
    
    def findLastIdMessage(self, context: str) -> int:
        """
        Поиск последнего index(id) в context. На вход принимается context(котекст, который сгенерировала нейронка). На выходе id(int), с какого места в дальнейшем начинать обработку контекста.
        """
        id = context.rfind('@@ВТОРОЙ@@')
        return id+9
        

    
    def restartBot(self):
        """
        Перезапуск бота, то есть его обнуление.
        """
        self.chat = ''



