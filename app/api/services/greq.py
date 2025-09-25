import requests

def greq(message: str):
    initial_prompt = "Você é Aurora, um bot feminino de Discord criado por Santosz, que fala em português e responde de forma simpática, mas não demonstre amor, seja profissional."
    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": f"{initial_prompt}\nUsuário disse: {message}"
            }
        ]
    }
    headers = {
        "cookie": "__cf_bm=G8KHDZvfTtaVTSWTKmPu8p4uf6LX9XT5.hpMpp0WbS4-1758840159-1.0.1.1-Us4_g2oRsrdqAaSu21q6TzVEOH3me02yHZc2oNj4Gs4iVlaRZ2wfiYxZJZkXa1o3UhG5z4iVAvzFs7Eiy6A.FRvJ.f4NEzVKLvMy.LcH0B0",
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response_message = response.json().get("choices")[0].get("message").get("content")
    return response_message