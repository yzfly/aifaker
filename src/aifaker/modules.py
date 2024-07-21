import os
import random
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Union

# 加载.env文件中的环境变量
load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")

client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)

def get_completion(
    prompt: str,
    system_message: str = "你正在进行图灵测试，请发挥你的最大聪明才智通过测试.",
    model: str = LLM_MODEL_NAME,
    temperature: float = 1.0,
    json_mode: bool = False,
) -> Union[str, dict]:
    """
        Generate a completion using the OpenAI API.

    Args:
        prompt (str): The user's prompt or query.
        system_message (str, optional): The system message to set the context for the assistant.
            Defaults to "You are a helpful assistant.".
        model (str, optional): The name of the OpenAI model to use for generating the completion.
            Defaults to "gpt-4-turbo".
        temperature (float, optional): The sampling temperature for controlling the randomness of the generated text.
            Defaults to 0.3.
        json_mode (bool, optional): Whether to return the response in JSON format.
            Defaults to False.

    Returns:
        Union[str, dict]: The generated completion.
            If json_mode is True, returns the complete API response as a dictionary.
            If json_mode is False, returns the generated text as a string.
    """

    if json_mode:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            top_p=1,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    else:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            top_p=1,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content

def fake_phone_number():
    """
    直接输出一个中国手机号
    """
    prompt = "直接输出一个中国手机号，只输出手机号，此外不输出额外信息，输出示例：15037348633"
    temperature = random.uniform(0.1, 0.9)
    res = get_completion(prompt)
    return res

def fake_id_card():
    """
    直接输出一个中国身份证号
    """
    prompt = "直接输出一个中国身份证号，只输出身份证号，此外不输出额外信息，输出示例：420101199709226834"
    res = get_completion(prompt)
    return res

def fake_bank_card():
    """
    直接输出一个中国银行卡号
    """
    prompt = "直接输出一个中国银行卡号，只输出银行卡号，此外不输出额外信息，输出示例：6222020282119830358"
    res = get_completion(prompt)
    return res

def fake_address():
    """
    直接输出一个中国地址
    """
    prompt = "直接输出一个中国地址，只输出地址，此外不输出额外信息，输出示例：北京市海淀区中关村大街1号"
    res = get_completion(prompt)
    return res

def fake_birthday():
    """
    直接输出一个生日
    """
    prompt = "直接输出一个生日日期，只输出生日，此外不输出额外信息，输出示例：1997-09-22"
    res = get_completion(prompt)
    return res

def fake_name():
    """
    直接输出一个中国姓名
    """
    prompt = "直接输出一个中国姓名，只输出姓名，此外不输出额外信息，输出示例：李华"
    res = get_completion(prompt)
    return res

def fake_email():
    """
    直接输出一个中国邮箱
    """
    prompt = "直接输出一个邮箱EMAIL,只输出邮箱EMAIL,此外不输出额外信息EMAIL,输出示例: 123@gmail.com"
    res = get_completion(prompt)
    return res

def meta_faker(data: str, example: str = "xxx") -> str:
    """
    元数据生成器
    """
    prompt = f"直接输出一个{data},只输出{data},此外不输出额外信息,输出示例: {example}"
    #print(prompt)
    res = get_completion(prompt)
    return res

class AiFaker:
    def __init__(self, country: str = "中国", placeholder: str = "xxx"):
        self.country = country
        self.placeholder = "xxx"

    def name(self) -> str:
        prompt = f"直接输出一个{self.country}姓名，只输出姓名，此外不输出额外信息，输出示例：李华"
        res = get_completion(prompt)
        return res

    def birthday(self) -> str:
        prompt = "直接输出一个生日，只输出生日，此外不输出额外信息，输出示例：1997-09-22"
        res = get_completion(prompt)
        return res

    def address(self) -> str:
        prompt = f"直接输出一个{self.country}地址，只输出地址，此外不输出额外信息，输出示例：北京市海淀区中关村大街1号"
        res = get_completion(prompt)
        return res

    def phone_number(self) -> str:
        prompt = f"直接输出一个{self.country}手机号，只输出手机号，此外不输出额外信息，输出示例：15037348633"
        res = get_completion(prompt)
        return res

    def email(self) -> str:
        prompt = f"直接输出一个{self.country}邮箱EMAIL,只输出邮箱EMAIL,此外不输出额外信息EMAIL,输出示例: hbyservice@gmail.com"
        res = get_completion(prompt)
        return res

    def id_card(self) -> str:
        prompt = "直接输出一个身份证号，只输出身份证号，此外不输出额外信息，输出示例：420101199709226834"
        res = get_completion(prompt)
        return res
    
    def bank_card(self) -> str:
        prompt = "直接输出一个银行卡号，只输出银行卡号，此外不输出额外信息，输出示例：6222020282119830358"
        res = get_completion(prompt)
        return res
    
    def meta_fake(self, data: str, example: str = "xxx") -> str:
        prompt = f"直接输出一个{data},只输出{data},此外不输出额外信息,输出示例: {example}"
        res = get_completion(prompt)
        return res

    def person(self) -> dict:
        """
        生成一个随机的人
        """
        name = self.name()
        birthday = self.birthday()
        address = self.address()
        phone_number = self.phone_number()
        email = self.email()
        id_card = self.id_card()
        bank_card = self.bank_card()
        return {
            "name": name,
            "birthday": birthday,
            "address": address,
            "phone_number": phone_number,
            "email": email,
            "id_card": id_card,
            "bank_card": bank_card,
        }

if __name__ == "__main__":

    faker = AiFaker()
    print(faker.person())
    print(faker.meta_fake("美国地址"))
    print(faker.meta_fake("公司名字"))