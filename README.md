
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
faker = AiFaker(country="en") # set the country to "en" for English, "cn" for Chinese

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
John Doe
1985-12-25
https://www.example.com
exampleuser@example.com
{'name': 'William Smith', 'birthday': '1985-12-15', 'address': 'https://www.google.com/', 'phone_number': '13745678901', 'email': 'exampleuser@example.com', 'id_card': '310107198501234567', 'bank_card': '6222020282119830358'}
13765432109
https://www.google.com/
1234 Main St, Anytown, USA, 12345
123-456-7890
```