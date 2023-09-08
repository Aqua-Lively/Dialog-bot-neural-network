import torch
from transformers import AutoTokenizer, AutoModelWithLMHead



class NeiroDialogBot:

    def __init__(self,model):
        self.tokenizer = AutoTokenizer.from_pretrained('app/model/save-model/tinkoff')
        self.model = AutoModelWithLMHead.from_pretrained('app/model/save-model/tinkoff')
        self.chat = ''
        self.idLastMessage = 0

    def replyToTheMessage(self,message):
        
        self.chat += f'@@ПЕРВЫЙ@@{message}@@ВТОРОЙ@@'
        self.idLastMessage = len(self.chat)-1
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

    def clearContext(self,context, id):
        string = ''
        id+=1
        while id < len(context) and context[id] != '@':
            string+= context[id]
            id+=1
        return string
    
    def findLastIdMessage(self,context):
        id = context.rfind('@@ВТОРОЙ@@')
        return id+9
        

    
    def restartBot(self):
        self.chat = ''
        self.idLastMessage = 0
        self.chat



