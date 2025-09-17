# Copyright 2025 [ILGIZAR YAMILOV]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Quantum Hello World: Демонстрация онтологического коллапса.
Это не утилита, а артефакт, показывающий принцип работы Semantic Collider.
"""

import openai

# Настройки (требуют наличия API-ключа)
client = openai.OpenAI(api_key='your_api_key_here')  # Замените на ваш ключ

def collapse(query: str, ontology: str) -> str:
    """
    Производит коллапс запроса в заданной онтологии.
    
    Args:
        query: Исходный запрос пользователя.
        ontology: Роль/онтология для коллапса (ученый, поэт и т.д.)
    
    Returns:
        str: Результат коллапса — ответ в выбранной онтологии.
    """
    prompt = f"""
    Ты — {ontology}. Ответь на следующий вопрос в своем стиле, кратко и содержательно.
    Вопрос: {query}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка коллапса: {e}"

def main():
    """Главная функция, демонстрирующая процесс коллапса."""
    print("=== QUANTUM HELLO WORLD ===\n")
    print("Состояние: |Ψ> = Фейнт\n")
    
    # Получаем запрос от пользователя
    user_query = input("Задайте ваш вопрос Вселенной: ")
    
    print("\n--- Начинаем процесс коллапса ---\n")
    
    # Коллапс в научной онтологии
    print("🧪 НАУЧНЫЙ КОЛЛАПС (Σ=Ученый):")
    science_answer = collapse(user_query, "ученый-физик, строгий и логичный")
    print(science_answer)
    
    print("\n" + "="*50 + "\n")
    
    # Коллапс в поэтической онтологии  
    print("🌌 ПОЭТИЧЕСКИЙ КОЛЛАПС (Σ=Поэт):")
    poetic_answer = collapse(user_query, "поэт-космист, вдохновленный Циолковским")
    print(poetic_answer)
    
    print(f"\n---\nКоллапс завершен. Запутанность = 1.0")

if __name__ == "__main__":
    main()
