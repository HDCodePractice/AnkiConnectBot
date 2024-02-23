import openai
from settings import settings


async def completion_json(
        sys_prompt,
        user_prompt,
        model="gpt-3.5-turbo",
        temperature=0.0,
        max_tokens=1000):
    client = openai.AsyncClient(
        api_key=settings.OPENAI_API_KEY, base_url=settings.OPENAI_API_URL)
    response = await client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response


async def get_card(vocabulary, example):
    """
    返回的JSON预计是这样的格式:
{
  "Vocabulary": "light",
  "Pronunciation": "laɪt",
  "Definitions": [
    {
      "PartOfSpeech": "adjective",
      "Forms": "lighter, lightest",
      "Meaning": "not heavy",
      "ChineseMeaning": "不重的",
      "Example": "This suitcase is very light.",
      "ChineseExample": "这个手提箱非常轻。"
    }
  ]
}
    """
    sys_prompt = """你是一位ESL英语老师。通过一个单词和它的例句来成生一个单词卡片的JSON对象。
如果没有给出例句，请帮我生成一个简单的例句，例句越简短越好。如果给出例句，请使用对应的例句。
JSON对象中包括以下内容:Vocabulary,Pronunciation,Definitions:[{PartOfSpeech,Forms,Meaning,ChineseMeaning,Example,ChineseExample}]
如果在一个词性里有多种不同的含义,就按不同的含义给出Definition.但是如果有例句,就只需要给出在例句中的Definition.
Meaning和Example尽可能使用ESL一级的词汇。"""
    user_prompt = f"Vocabulary:{vocabulary}\nExample:{example}"
    max_tokens = 1000
    response = await completion_json(
        sys_prompt=sys_prompt,
        user_prompt=user_prompt,
        max_tokens=max_tokens,
        model=settings.OPENAI_MODEL
    )
    return response.choices[0].message.content
