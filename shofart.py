import logging
from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def hello():
    welcome = "Welcome to shofart! Which shofar blow would you like? "
    return question(welcome).reprompt(welcome + 'You can ask for tekiah, shevarim, teruah, or tekiah gedolah.')



@ask.intent("ShofarCallIntent")
def shofar_blast(shofar_call):

    tekiah_mp3 = 'https://www.dropbox.com/s/90raxeb900rwmnp/Tekiah.mp3?dl=0'

    audit_msg = '<speak><audio src="{}" /></speak>'

    try:

        if not shofar_call:
            msg = 'I did not hear a shofar call. Please try again. You can say tekiah, shevarim, teruah, or tekiah gedolah. '


        elif shofar_call == 'tekiah':
            msg = audit_msg.format(tekiah_mp3)


        else:
            msg = 'I did not hear a shofar call. Please try again. You can say tekiah, shevarim, teruah, or tekiah gedolah. '

        return statement(msg).simple_card('Shofart', msg)


    except Exception as e:
        msg = "Error: {}.".format(e)

        return statement(msg).simple_card('Shofart', msg)



@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = "Shofart! Woot toot! "
    reprompt_text = 'What shofar call would you like?'
    return question(speech_text).reprompt(reprompt_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    msg = 'Bye bye!'
    return statement(msg)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    msg = 'Bye bye!'
    return statement(msg)


if __name__ == '__main__':
    # print(shofar_blast('tekiah').__dict__)
    app.run(debug=True)