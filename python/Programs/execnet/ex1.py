import execnet

def exec_code_string_in_sub_proc():
    """source is a string: execute source string remotely with a channel put into the global namespace.

    """
    gw = execnet.makegateway()
    channel = gw.remote_exec("channel.send(channel.receive() + 1)")
    channel.send(1)
    out = channel.receive()
    gw.exit()
    print("\nout: {0}\n".format(out))

def multiplier(channel, factor):
    while(not channel.isclosed()):
        global abc
        input = channel.receive()
        result = input * 2
        channel.send(result)

def exec_method_in_sub_process():
    gw = execnet.makegateway()
    channel = gw.remote_exec(multiplier, factor = 10)
    channel.send(2)
    out = channel.receive()
    gw.exit()
    print("\nOut:{0}\n".format(out))

def main():
    #exec_code_string_in_sub_proc()
    exec_method_in_sub_process()

if __name__ == '__main__':
    main()
