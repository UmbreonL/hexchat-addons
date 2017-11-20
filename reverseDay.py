import hexchat, random

__module_name__ = "Reverse day"
__module_version__ = "0.1"
__module_description__ = "SANICK joining nicks to fitting theme: Reversed"


config = {
    # We will only work at this IRC network.
    "network": "yourIRCNetwork",

    # We will monitor the userJoin events of this channel.
    "channel": "#yourChannel",

    # These names will not be affected by a Pokémon name.
    "override": ["nick1", "nick2"],
}

def userJoin(word, word_eol, userdata):
    if hexchat.get_info('network') == config["network"] and hexchat.get_info("channel") == config["channel"]:
        if word[0].lower() in config["override"]:
            pass
        else:
            if word[0][::-1].lower() == ident.lower():
                word[0] = word[0][::-1]
            else:
                if hasNumbers(word[0]):
                    word[0] = ''.join([i for i in word[0] if not i.isdigit()])
                    hexchat.command("sanick %s %s" % (word[0], word[0][::-1]))  
                else:
                    hexchat.command("sanick %s %s" % (word[0], word[0][::-1]))
hexchat.hook_print("Join", userJoin)

def revnick(word, word_eol, userdata):
    try:
        word[1]
        print(word[1])
    except IndexError:
        print("Please enter a nick.")
    else:
        word.pop(0)
        for name in word:
            newNick = newNick = word[1][::-1]
            hexchat.command("sanick %s %s" % (name, newNick.title()))
hexchat.hook_command("revnick", revnick)