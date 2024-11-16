from piazza_api import Piazza
import os 
from dotenv import load_dotenv
from html2text import HTML2Text
from bot import prompt

HTML_2_TEXT = HTML2Text()
HTML_2_TEXT.ignore_links = True

load_dotenv()

EMAIL = str(os.getenv("EMAIL"))
PASSWORD = str(os.getenv("PASSWORD"))




p = Piazza()

p.user_login(email = EMAIL, password = PASSWORD)

course = p.network("m09vgkjb1t96r0") #  Add your own class id

posts = course.iter_all_posts(limit = 40)
prompts = ""
for post in posts:
    post_content = post['history'][0]['content']
    post_content_as_text = HTML_2_TEXT.handle(post_content)
    prompts+=post_content_as_text+"\n\n\n"
print(prompt("Classify the following posts into categories and write a summary: "+prompts))
# print(prompt("Generate a list of frequently asked questions from the following questions:"+prompts))
# print(prompt("Group similar posts in the following posts together: "+prompts))