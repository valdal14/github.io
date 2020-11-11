import os
import random
from datetime import datetime
import time

commits = [
  'Updated the css file',
  'Modified the js file',
  'Changed the js logic to load the images',
  'Updated the index.html file'
]

while True:
  c = random.randint(0, len(commits) - 1)

  now = datetime.now()
  dt_string = now.strftime("%H:%M")

  if dt_string == "16:23":
    try:
      with open('README.md', 'a+') as f:
        f.write(commits[c] + '\n') 
    except FileNotFoundError as e:
      print('File not found')

    os.system('git add .')
    git_comment = str("git commit -m {}{}{}".format("'", commits[c], "'"))

    os.system(git_comment)
    os.system("git push -u origin master")
    break
  else:
    print('Nothing to push')
    time.sleep(30)
