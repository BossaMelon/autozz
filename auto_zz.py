import itchat
from itchat.content import PICTURE, RECORDING, ATTACHMENT, VIDEO, TEXT

itchat.auto_login(hotReload=True, enableCmdQR=True)
namelist = []


@itchat.msg_register([TEXT])
def print_content(message):
    user_name = itchat.search_friends(userName=message['FromUserName'])
    from_user = user_name["NickName"]
    if '骂我' in message['Text']:
        if from_user in namelist:
            return '说一次就够了，智障'
        else:
            namelist.append(from_user)
        show_name()
    if message['Text'] == '我错了':
        if from_user in namelist:
            namelist.remove(from_user)
            show_name()
            return '辣鸡'
    if from_user in namelist:
        return "你是智障"


@itchat.msg_register([PICTURE])
def print_content(message):
    user_name = itchat.search_friends(userName=message['FromUserName'])
    from_user = user_name["NickName"]
    if from_user in namelist:
        return "发图的都是智障"


@itchat.msg_register([RECORDING])
def print_content(message):
    user_name = itchat.search_friends(userName=message['FromUserName'])
    from_user = user_name["NickName"]
    if from_user in namelist:
        return "发语音的也是智障"


@itchat.msg_register([ATTACHMENT])
def print_content(message):
    user_name = itchat.search_friends(userName=message['FromUserName'])
    from_user = user_name["NickName"]
    if from_user in namelist:
        return "发文件是智障"


def show_name():
    print('current name: ')
    for i in namelist:
        print(i)


def run():
    show_name()
    itchat.run(True)


if __name__ == '__main__':
    run()
