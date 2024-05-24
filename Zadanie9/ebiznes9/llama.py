import ollama


def ask_llama2(content):
    response = ollama.chat(model='llama2', messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    return response['message']['content']
