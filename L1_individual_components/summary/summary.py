import google.generativeai as genai

from config import GOOGLE_API_KEY


class Summary:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

    def getSummary(self, nerText, plainText):
        try:
            response = self.model.generate_content(
                [
                    f'input: * **Document:** "{plainText}" * **NER Results:** "{nerText}"',
                    "output: ",
                ]
            )
            return response.text
        except Exception as err:
            print(f"Error occurred while creating summary: {err}")
            raise Exception("Error occurred in summary component") from err
