""" 
Full assembly of the parts to form the complete network 

Adapted from https://github.com/milesial/Pytorch-UNet
"""

import torch.nn.functional as F

from unet_parts import *


class UNet(nn.Module):
    def __init__(self, n_channels, n_classes, bilinear=True):
        super(UNet, self).__init__()
        
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.bilinear = bilinear

        # input 44x44
        self.inc = DoubleConv(n_channels, 16)
        # input 40x40
        self.down1 = Down(16, 16)
#         self.down2 = Down(128, 256)
#         self.down3 = Down(256, 512)
#         self.down4 = Down(512, 512)
#         self.up1 = Up(1024, 256, bilinear)
#         self.up2 = Up(512, 128, bilinear)
#         self.up3 = Up(256, 64, bilinear)
        # input 16x16
        self.up4 = Up(32, 8, bilinear)
        # input 28x28
        self.outc = OutConv(8, n_classes)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
#         x3 = self.down2(x2)
#         x4 = self.down3(x3)
#         x5 = self.down4(x4)
#         x = self.up1(x5, x4)
#         x = self.up2(x, x3)
#         x = self.up3(x, x2)
        x = self.up4(x2, x1)
        print(x2.shape)
        #logits = self.outc(x)
        return x