import asyncio
from openai import AsyncOpenAI
from openai import APIError, RateLimitError
from config import settings
from .data_changer import data_to_string


client = AsyncOpenAI(api_key=settings.get_ds_api_key,
                     base_url='https://api.deepseek.com')


async def get_message(data: dict) -> dict:
    print('Запрос пришел')
    try:
        response = await client.chat.completions.create(
            model='deepseek-chat',
            messages=[
                {'role': 'system', 'content': 'Сделай пару простых выводов о том как я распоряжаюсь '
                'деньгами на основе этих данных, постарайся уложиться в 2 или 3 предложения.'},
                {'role': 'user', 'content': await data_to_string(data)}
            ],
            temperature=0.6,
            max_tokens=200
        )

        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except RateLimitError:
        print("⚠️ Превышен лимит запросов. Подождите немного.")
        return 'Нет анализа ИИ'
    except APIError as e:
        print(f"⚠️ Ошибка API: {e}")
        return 'Нет анализа ИИ'
    except Exception as e:
        print(f"⚠️ Неизвестная ошибка: {e}")
        return 'Нет анализа ИИ'
