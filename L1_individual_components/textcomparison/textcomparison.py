import google.generativeai as genai

from config import GOOGLE_API_KEY


class TextComparison:
    def __init__(self, paragraphs_template, paragraphs_contract):
        self.paragraphs_template = paragraphs_template
        self.paragraphs_contract = paragraphs_contract
        self.dict = ()
        self.model = None

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

    def individual_comparator(self, template_text, contract_text):
        try:
            prompt = (
                'input: "template text": "' + str(template_text) + '"\n\n'
                '"contract text": "' + str(contract_text) + '"\n\n'
                "query: find the differences in the contract text in the context "
                "of the template text and provide them briefly"
            )
            result = self.model.generate_content([prompt])
            return result.text
        except Exception as err:
            print(f"Error occurred while comparing PDF: {err}")
            return ""

    def comparator(self):
        headings = []
        comparisons = []

        for heading, paragraph in self.paragraphs_contract.items():
            if heading in self.paragraphs_template:
                result = self.individual_comparator(
                    self.paragraphs_template[heading],
                    paragraph,
                )
                headings.append(heading)
                comparisons.append(result)
            else:
                print(
                    "Heading is missing from the provided template. "
                    "Skipping comparison."
                )

        self.dict = tuple(zip(headings, comparisons))
        return self.dict

    def printComparison(self):
        for key, value in self.dict:
            print(f"Key: {key}, Value: {value}")
