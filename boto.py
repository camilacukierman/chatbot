"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json


list_boto = {
    "camila":{"msg": "Hello, lest talk..,","animation":"dancing"},
    "felling": {"msg":"I am fine","animation":"excited"},
    "hobby": {"msg":"i like to do some code....","animation":"heartbroke"},
    "movie":{"msg":"the beauty and the beast","animation":"inlove"},
    "sport":{"msg":"i dont like sport, i like dancing","animation":"dancing"},
    "music":{"msg":"mizhrari","animation":"ok"},
    "drink":{"msg":"cola zero, is the best","animation":"excited"},
    "food":{"msg":"sushi, do u want to invite me to eat some sushi tonigth?","animation":"inlove"},
    "love": {"msg": "of course i love u.... do you love ", "animation": "inlove"}
}


@route('/', method='GET')
def index():
    return template("chatbot.html")


def handleSimpleAsnwers(msg):
    if msg.lower() == "yes":
        return {"msg":"I love you !thanks for beeing so nice","animation":"inlove"}
    if msg.lower() == "no":
        return {"msg": "dont ne rude....", "animation": "no"}
    return None

def handleBadWords(msg):
    if msg.startswith("fuck you"):
        return {"msg":"lama cacha? fuck u too","animation":"takeoff"}
    return None



@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    result = handleSimpleAsnwers(user_message)
    result = handleBadWords(user_message)
    if not result:
        for word in user_message.split(" "):
            if word in list_boto:
                return json.dumps(list_boto[word])

        return json.dumps({"animation": "giggling", "msg": "I don't understand,sorry"})
    return json.dumps(result)


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
