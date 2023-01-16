import base64logic as el
import CaesarsCipherLogic as cl
import EncoderDecoderView as ev

if __name__ == '__main__':
    logic = cl.Logic()
    view = ev.EncoderDecoderView(logic)