import g4f

class Gpt:
    def __init__(self, prompts='Привет, ты работаешь?', proxy:str | None='socks5://42090:Fvsd45@176.106.53.179:42090'):
        self.prompts = prompts
        self.cnt = 0
        self.conf_prompt = 'Rewrite the following text to make it more sarcastic in russian language:'
        self.output1 = ''
        self.output = []
        self.output_talk = ''
        self.proxy = proxy
    
            
    def talk_valid_markdown(self, prompts:str='Привет, ты работаешь?'):
            messages = [{"content": prompts, "role": "user"}]
            
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                provider=g4f.Provider.Bing,
                messages=messages,
                proxy=self.proxy
            )

            return response.replace('**', '*')
