#!.venv/bin/python
import sys,os,tty,termios

import click
import colorful
import numpy as np
from PIL import Image

IMG = './img/logo.png'

@click.command()
@click.option('--width', default=128)
@click.option('--height', default=64)
@click.option('--scale', default=16)
@click.argument('imgpath')
def main(width, height, scale, imgpath):
    colorful.use_true_colors()
    np.set_printoptions(formatter={'int': lambda x: format(x, 'x')})

    im_origin = Image.open(imgpath)
    _w, _h = im_origin.size

    k = 0
    x0 = 0
    y0 = 0

    im = im_origin.copy()
    w, h = _w // scale, _h // scale
    im.thumbnail((w, h), Image.ANTIALIAS)
    img = np.asarray(im.convert('RGBA')).astype(np.int32)
    tdraw(img, x0, y0, width, height)

    while k != 'q':
        if k == 'h':
            x0 -= 1
            x0 = max(0, x0)
            tdraw(img, x0, y0, width, height)
        elif k == 'j':
            y0 += 1
            y0 = min(img.shape[1], y0)
            tdraw(img, x0, y0, width, height)
        elif k == 'k':
            y0 -= 1
            y0 = max(0, y0)
            tdraw(img, x0, y0, width, height)
        elif k == 'l':
            x0 += 1
            x0 = min(img.shape[1], x0)
            tdraw(img, x0, y0, width, height)
        elif k == '':
            x0 -= width // 2
            x0 = max(0, x0)
            tdraw(img, x0, y0, width, height)
        elif k == '':
            y0 += height // 2
            y0 = min(img.shape[0] - height, y0)
            tdraw(img, x0, y0, width, height)
        elif k == '':
            y0 -= height // 2
            y0 = max(0, y0)
            tdraw(img, x0, y0, width, height)
        elif k == '':
            x0 += width // 2
            x0 = min(img.shape[1] - width, x0)
            tdraw(img, x0, y0, width, height)
        elif k == '+':
            _scale = scale
            scale -= 1
            scale = max(scale, 1)
            x0 = x0 * _scale // scale
            y0 = y0 * _scale // scale
            w, h = _w // scale, _h // scale
            im = im_origin.copy()
            im.thumbnail((w, h), Image.ANTIALIAS)
            img = np.asarray(im.convert('RGBA')).astype(np.int32)
            tdraw(img, x0, y0, width, height)
        elif k == '-':
            _scale = scale
            scale += 1
            x0 = x0 * _scale // scale
            y0 = y0 * _scale // scale
            w, h = _w // scale, _h // scale
            im = im_origin.copy()
            im.thumbnail((w, h), Image.ANTIALIAS)
            img = np.asarray(im.convert('RGBA')).astype(np.int32)
            tdraw(img, x0, y0, width, height)
        k = getch()

def tdraw(img, x1, y1, w, h):
    print('\033[0;0H')
    cache = ''
    x2 = x1 + w
    y2 = y1 + h
    x2 = min(img.shape[1], x2)
    y2 = min(img.shape[0], y2)
    for y in range(y1, y2-1, 2):
        for x in range(x1, x2):
            cache += printc('\u2580',
                   fg=img[y, x, :3]*img[y, x, 3]//255,
                   bg=img[y+1, x, :3]*img[y+1, x, 3]//255)
        cache += '\n'
    cache += 'type q for quit'
    sys.stdout.write(cache)
    sys.stdout.flush()

def printc(content, fg='#000000', bg='#ffffff'):
    colorful.use_palette({'fg': fg, 'bg': bg})
    return str(colorful.fg_on_bg(str(content)))

def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

if __name__ == "__main__":
    main()
