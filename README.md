# terimg
display image in terminal

[![demo](https://asciinema.org/a/252886.svg)](https://asciinema.org/a/252886?autoplay=1)

## install
make virtual environment
```shell
make init
```
install dependencies
```shell
make install
```
## usage
run example
```shell
./ti.py --width=100 --height=64 --scale=10 path/to/img.png
```
move one pixel with `h, j, k, l`.
move half width/height of window with `Ctrl-h, Ctrl-u, Ctrl-d, Ctrl-l`.
zoom with +, -.
quit with q.

## option
`--width` set the width of window  
`--height` set the height of window  
`--scale` resize the entire image with 1/scale
