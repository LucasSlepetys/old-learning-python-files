from nylas_token import CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN
from nylas import APIClient

nylas = APIClient(
    CLIENT_ID,
    CLIENT_SECRET,
    ACCESS_TOKEN,
)

# list_email = []
# with open('halloween_email.txt') as f:
#     for line in f:
#         list_email.append((line.split("\n")[0]).lower())

# left = len(list_email)
count = 3
email = "samuel_weisz@fis.edu"
while count > 0:
    print(count)

    draft = nylas.drafts.create()
    name = email.split("_")[0]
    name = name[0:1].upper() + name[1:]
    title = str("Yooooo " + name.upper() + "!")

    body_message = name + " heheeh"

    draft.subject = title
    draft.body = body_message

    draft.to = [{'name': title, 'email': email}]

    draft.send()

    count -= 1

print("done")