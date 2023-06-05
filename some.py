import openai
import json
from base64 import b64decode
import os
import subprocess

with open(os.path.dirname(os.path.realpath(__file__)) + "/api_key.txt") as file:
    API_KEY = file.readline().strip()
    API_KEY = API_KEY[1:-1]


def image_generator(user_input):
    prompt = user_input
    openai.api_key = API_KEY

    response = openai.Image.create(
        prompt=prompt, n=1, size="1024x1024", response_format="b64_json"
    )

    with open("data.json", "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    image_data = b64decode(response["data"][0]["b64_json"])
    file_name = "_".join(prompt.split(" "))

    with open(f"{file_name}.png", "wb") as file:
        file.write(image_data)

    result = subprocess.run(
        ["imgur-uploader", f"{file_name}.png"], capture_output=True, text=True
    ).stdout
    length = len(result)

    os.remove(f"{file_name}.png")

    return result[length - 33 : length - 1]


# s = input("Enter your text: ")
# image_generator(s)
