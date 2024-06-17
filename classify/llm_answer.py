import time
import os
import yaml
from langchain.prompts import PromptTemplate
from openai import AzureOpenAI

class GPTAnswer:
    TOP_K = 10

    def __init__(self):
        # Update the config path to ensure it points to the correct location
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
        self.deployment_name = self.config[deployment_name]
        self.model_name = self.config[model_name]
        self.template = self.config[template]

    def start_conversation(self, message):
        # 发送对话请求
        client = AzureOpenAI(
            azure_endpoint='', 
            api_key='',  
            api_version="",
            )
        response = client.chat.completions.create(
            model=self.model_name,
            messages=message,
            temperature=0.5,
            top_p=0.95,
            frequency_penalty=0,
            max_tokens=4000,
            stop=None
        )
        return response.choices[0].message.content.strip()

    def classify_github_issue(self, title, body):
        prompt_template = PromptTemplate(input_variables=["title","body"], template=self.template)
        summary_prompt = prompt_template.format(title=title, body=body)
        print("\n\nThe message sent to LLM:\n", summary_prompt)
        print("\n\n", "="*30, "GPT's Answer: ", "="*30, "\n")
        
        message = [{"role": "system", "content": summary_prompt}]
        
        # 使用 start_conversation 方法发送请求
        gpt_answer = self.start_conversation(message)
        
        return gpt_answer
