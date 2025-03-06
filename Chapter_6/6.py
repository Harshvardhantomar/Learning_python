favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}

poll_participants = ['Simon','JJ','Harry','Vik','Harsh']

favorite_poll = ['jen','harsh','sarah','muskan','aditya','tanmay','harry','vik']

for people in favorite_poll:
    if(people.title() in poll_participants):
        print(f"Thanks! {people.title()} for taking part in the poll.\n")
    else:
        print(f"Hey {people.title()}, would you like to take a poll?\n")