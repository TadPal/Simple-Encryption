import EncodeLogics.base64logic as el
import EncodeLogics.CaesarsCipherLogic as cl
import EncodeLogics.RSALogic as rsa

import TkinterView.EncoderDecoderView as ev
import TkinterView.EncoderDecoderRSAView as rsav

if __name__ == '__main__':
    logic = rsa.Logic()
    view = rsav.EncoderDecoderView(logic)