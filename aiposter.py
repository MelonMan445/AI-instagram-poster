import io
import tempfile
from PIL import Image
from instabot import Bot
from image_caption_ai_func import generate_instagram_post  

def login():
    bot = Bot()

    while True:
        username = input("Enter your Instagram username: ")  
        password = input("Enter your Instagram password: ")  

        # Attempt login
        try:
            bot.login(username=username, password=password, use_cookie=False, cookie_fname="cookie.txt")
            print("Logged in successfully!")
            break  
        except Exception as e:
            print(f"Login failed. Please try again. Error: {e}")
           

    
    while True:
        prompt = input("Enter a prompt for your Instagram post: ")
        if not prompt:
            print("Prompt cannot be empty. Please try again.")
            continue

        try:
            
            image, caption = generate_instagram_post(prompt)
            image.show()  
            print("\nGenerated Caption:", caption)

            
            post_decision = input("Do you want to post this image? (yes/no): ").strip().lower()

            if post_decision == "yes":
               
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                    
                    image.save(temp_file, format="JPEG")
                    temp_file.close()  
                
                   
                    bot.upload_photo(temp_file.name, caption=caption)
                    print("Posted successfully!")
            else:
                print("Post not made. Let's try again with a new prompt.")

        except ValueError as e:
            print("Error:", str(e))

        continue_decision = input("Do you want to create a new post? (yes/no): ").strip().lower()
        if continue_decision != "yes":
            print("Exiting... Goodbye!")
            break

if __name__ == "__main__":
    login()
