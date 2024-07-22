
# AiFaker

AiFaker is a Python library that uses the LLM API to generate fake data for various purposes. It provides a simple and easy-to-use interface for generating fake names, birthdays, addresses, emails, and more.

## Suggestions:
You can visit [siliconflow](https://siliconflow.cn/zh-cn/pricing) for free LLM API key and base URL, and you can use the Qwen/Qwen2-7B-Instruct model for free.
 
## 🚀 Quick Start

### 📦 Installation

```bash
pip install aifaker
```

### Basic Usage
```
import os
from aifaker import AiFaker

# set the environment variables
os.environ["LLM_API_KEY"] = "sk-xxx"  # replace with your API key
os.environ["LLM_BASE_URL"] = "https://api.siliconflow.cn/v1" # replace with your base URL
os.environ["LLM_MODEL_NAME"] = "Qwen/Qwen2-7B-Instruct" # replace with your model name

# create an instance of the AiFaker class
faker = AiFaker(country="zh") # set the country to "en" for English, "cn" for Chinese

# generate a fake name
print(faker.name())

# generate a fake birthday
print(faker.birthday())

# generate a fake address
print(faker.address())

# generate a fake email
print(faker.email())

# generate a fake person
print(faker.person())

# generate a fake phone number
print(faker.phone_number())

# generate a fake address
print(faker.address())

# generate anything you want just by passing in the data description
print(faker.meta_fake(data="美国地址"))

# generate anything you want just by passing in the data description and example
print(faker.meta_fake(data="美国手机号", example="123-456-7890"))
```

The results should be like:
```
张三
1985-12-15
上海市徐汇区漕溪北路595号
example_zh_account@sample.com
{'name': '张伟', 'birthday': '2000-03-15', 'address': '上海市浦东新区陆家嘴环路1088号', 'phone_number': '13612345678', 'email': 'icebergmailuser@gmail.com', 'id_card': '310107199005017276', 'bank_card': '6222020282119830358'}
13812345678
北京市海淀区知春路甲45号量子银座18层
123 Main St, Anytown, USA, 12345
135-432-1098
```