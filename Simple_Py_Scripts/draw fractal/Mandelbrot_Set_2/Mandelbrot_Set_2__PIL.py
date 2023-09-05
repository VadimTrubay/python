#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""
Множество Мандельброта 2 / Mandelbrot Set 2

"""


# Оригинал: http://www.cyberforum.ru/pascalabc/thread994987.html
# uses GraphABC;
#
# const
#   n=255;
#   max=10;
#
# var
#   x,y,x1,y1,cx,cy: real;
#   i,ix,iy: integer;
# // z=z^2+c
# begin
#   SetWindowSize(600,600);
#   SetWindowCaption('Фракталы: множество Мандельброта');
#   for ix:=0 to WindowWidth-1 do
#   for iy:=0 to WindowHeight-1 do
#   begin
#     x:=0;
#     y:=0;
#     cx:=0.005*(ix-365);
#     cy:=0.005*(iy-300);
#     for i:=1 to n do
#     begin
#       x1:=x*x-y*y+cx;
#       y1:=2*x*y+cy;
#       if (x1>max) or (y1>max) then break;
#       x:=x1;
#       y:=y1;
#     end;
#     if i>=n then SetPixel(ix,iy,clRed)
#       else SetPixel(ix,iy,RGB(255,255-i,255-i));
#   end;
# end.


def draw_mandelbrot_set_2(draw_by_image, width, height):
    n = 255
    max = 10
    
    for ix in range(width):
        for iy in range(height):
            x = 0
            y = 0
            cx = 0.005 * (ix - 365)
            cy = 0.005 * (iy - 300)
    
            for i in range(n):
                x1 = x * x - y * y + cx
                y1 = 2 * x * y + cy
    
                if x1 > max or y1 > max:
                    break
    
                x = x1
                y = y1

            if i >= n:
                color = "red"
            else:
                color = (255, 255 - i, 255 - i)

            draw_by_image.point((ix, iy), color)


if __name__ == '__main__':
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (600, 600), "white")

    draw_mandelbrot_set_2(ImageDraw.Draw(img), img.width, img.height)

    img.save('img.png')
