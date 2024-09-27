import os

import dotenv
from groq import Groq

dotenv.load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY"),
)

text_file_path = "a.html"
with open(text_file_path, "r", encoding="utf-8") as f:
    text = f.read()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """
                あなたは日本語の優秀な要約者です。
                大学の研究機関のプレスリリースのテキストを渡します。
                そのテキストを以下の形式で要約してください。

                # 注意！
                - jsonだけを返してください。
                - 日本語で返答してください。

                # 出力の例
                {{
                    "title": "",
                    "date": "",
                    "background": "",
                    "summary": "",
                    "researchers": [
                        {{
                            "name": "",
                            "affiliation": ""
                        }}
                    ],
                }}
            """,
        },
        {
            "role": "user",
            "content": text,
        }
    ],
    model="llama3-8b-8192",
    # model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)
