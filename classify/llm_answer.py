import os
import yaml
from openai import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import AzureOpenAI as LangChainAzureOpenAI


class GPTAnswer:
    TOP_K = 10

    def __init__(self):
        # Update the config path to ensure it points to the correct location
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
        self.deployment_name = ''
        self.model_name = ''
        self.template = self.config["template"]
        self.azure_endpoint = '/'
        self.api_key = ''
        self.api_version = '2024-02-01'
        self.client = LangChainAzureOpenAI(
            endpoint=self.azure_endpoint,
            api_key=self.api_key,
            api_version=self.api_version,
            deployment_name=self.deployment_name,
            model_name=self.model_name
        )

    def start_conversation(self, message):
        llm_chain = LLMChain(
            llm=self.client,
            prompt=message,
        )
        response = llm_chain.run()
        return response.strip()

    def classify_github_issue(self, title, body):
        prompt_template = PromptTemplate(
            input_variables=["title", "body"],
            template=self.template
        )
        summary_prompt = prompt_template.format(title=title, body=body)
        print("\n\nThe message sent to LLM:\n", summary_prompt)
        print("\n\n", "="*30, "GPT's Answer: ", "="*30, "\n")
        
        # 使用 start_conversation 方法发送请求
        gpt_answer = self.start_conversation(summary_prompt)
        print(gpt_answer)
        
        return gpt_answer