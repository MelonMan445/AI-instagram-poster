import requests
from PIL import Image
from io import BytesIO
import urllib.parse
import google.generativeai as genai

def generate_instagram_post(prompt, safe=True):
    """
    Generates both an AI image and a matching Instagram caption based on a prompt.

    Args:
        prompt (str): The base prompt for generating both image and caption.
        safe (bool): Whether to use safe mode for image generation.

    Returns:
        tuple: (PIL Image object, str) containing the generated image and caption.

    Raises:
        ValueError: If the prompt is missing or API responses are invalid.
    """
    if not prompt:
        raise ValueError("Prompt must be provided.")

    # First, generate the image
    def generate_image(image_prompt):
        # Fixed parameters
        width, height = 1024, 1024
        model = 'flux'

        # Construct the base URL with the prompt
        url_prompt = urllib.parse.quote(image_prompt)
        image_url = f"https://image.pollinations.ai/prompt/{url_prompt}"

        # Add parameters
        params = [
            f"width={width}",
            f"height={height}",
            "nologo=true",
            "enhance=true",
            f"model={model}"
        ]

        if not safe:
            params.append("safe=false")

        image_url += '?' + '&'.join(params)

        # Fetch the image
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            return Image.open(image_data)
        else:
            raise ValueError(f"Failed to fetch image. Status code: {response.status_code}")

    # Generate caption using Google AI
    def generate_caption(base_prompt):
        try:
            API_KEY = ""#add you google gemini ai api key 
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel("")#select thw model you are using
            
            caption_prompt = f"""
            Create an engaging Instagram caption for an image with this description: '{base_prompt}'
            
            Requirements:
            - Keep it under 200 characters
            - Include 2-3 relevant hashtags
            - Make it engaging and authentic
            - Don't use excessive emojis (max 2)
            - Maintain a casual, friendly tone
            """
            
            response = model.generate_content(caption_prompt)
            return response.text.strip()
        except Exception as e:
            raise ValueError(f"Caption generation failed: {str(e)}")

    # Generate both image and caption
    try:
        image = generate_image(prompt)
        caption = generate_caption(prompt)
        
        return image, caption
    except Exception as e:
        raise ValueError(f"Post generation failed: {str(e)}")
