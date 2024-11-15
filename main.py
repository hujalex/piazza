from piazza_api import Piazza
import os 
from dotenv import load_dotenv
from html2text import HTML2Text

HTML_2_TEXT = HTML2Text()
HTML_2_TEXT.ignore_links = True

load_dotenv()

EMAIL = str(os.getenv("EMAIL"))
PASSWORD = str(os.getenv("PASSWORD"))


print(EMAIL)


p = Piazza()

p.user_login(email = EMAIL, password = PASSWORD)

course = p.network("m08oofbzpg02wn") #  Add your own class id

posts = course.iter_all_posts(limit = 10)
for post in posts:
    post_content = post['history'][0]['content']
    post_content_as_text = HTML_2_TEXT.handle(post_content)
    print(post_content_as_text)

