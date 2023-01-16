import base64logic as el
import CaesarsCipherLogic as cl
import RSALogic as rsa

import EncoderDecoderView as ev
import EncoderDecoderRSAView as ersa

if __name__ == '__main__':
    logic = rsa.Logic()
    view = ersa.EncoderDecoderView(logic)