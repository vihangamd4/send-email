import yagmail
import os
import time
from datetime import datetime as dt

sender = 'vihangawork1@gmail.com'
receiver = 'vihangamd4@gmail.com'

subject = "test1"
contents = """bla bla 
bla
"""

yag = yagmail.SMTP(user=sender , password=os.getenv('PASSWORD'))

while True:
  now = dt.now()
  if now.hour == 20 and now.minute == 47:
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent!")
    time.sleep(60)
  


