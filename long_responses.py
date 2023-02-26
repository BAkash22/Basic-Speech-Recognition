import random

R_tamil = "Vannakam Nanba!"
R_Name = "My name is AK bot"
R_who = "Iam a chatbot limited-AI, i Cant answer too many questions"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "sorry,What does that mean?"][
        random.randrange(4)]
    return response