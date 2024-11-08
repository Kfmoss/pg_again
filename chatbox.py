import aiml
import webbrowser as wd




kernel = aiml.Kernel() ##load library
kernel.learn("startup.xml")
kernel.respond("LOAD AIML B")

while True:
    input_text= input(">You: ")
    response = kernel.respond(input_text)
    print(">Bot: "+response)