import os
import openai
from openai import OpenAIError, RateLimitError, APIConnectionError
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt, engine=None, max_tokens=1000, retries=3):
    """
    Generate text using OpenAI's GPT-3 model.

    :param prompt: The prompt to send to the model.
    :param engine: The engine/model to use for the completion. Defaults to environment setting or 'text-davinci-002'.
    :param max_tokens: The maximum number of tokens to generate.
    :param retries: The maximum number of retries in case of rate limit or connection errors.
    :return: A tuple containing (generated_text, error_message).
    """
    if engine is None:
        engine = os.getenv('OPENAI_ENGINE', 'text-davinci-002')

    attempt = 0
    while attempt < retries:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                max_tokens=max_tokens
            )
            generated_text = response.choices[0].text.strip()
            return generated_text, None
        except (RateLimitError, APIConnectionError) as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
            attempt += 1
        except OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            return None, f"An error occurred while generating the text: {str(e)}. Please try again later."
    return None, "Max retries exceeded. Please try again later."

