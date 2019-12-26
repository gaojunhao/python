while True:
    try:
        print('go to try\n')
        a = 1 / 0
    except ValueError:
        print('try command is error\n')
    except:
        print('can not find the type of error\n')
        raise Exception('have an error')
    else:
        print('go to else loop\n')
    finally:
        print('go to finally loop\n')
