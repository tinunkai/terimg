# terimg
display image in true color capable linux/unix terminal (not supporting windows)

[![demo](https://asciinema.org/a/252886.svg)](https://asciinema.org/a/252886?autoplay=1)

## Install
make virtual environment
```shell
make init
```
install dependencies
```shell
make install
```
## Usage
run example
```shell
./ti.py --width=100 --height=64 --scale=10 path/to/img.png
```
move one pixel with `h, j, k, l`  
move half width/height of window with `Ctrl-h, Ctrl-u, Ctrl-d, Ctrl-l`  
zoom in/out with `i, o`, scale=1 with `0`  
quit with `q`

## Option
`--width` set the width of window  
`--height` set the height of window  
`--scale` resize the entire image with 1/scale

## License
MIT
