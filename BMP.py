def write_grayscale(filename, pixels):

    """creates a grayscale BMP file"""

height = len(pixels)
width = len(pixels[0])

with open(filename, 'wb') as bmp:
    #BMP Header
    bmp.write(b'BM')

    size_bookmark = bmp.tell()
    bmp.write(b'\x00\x00\x00\x00')

    bmp.write(b'\x00\x00')
    bmp.write(b'\x00\x00')

    pixel_offset_bookmark = bmp.tell()
    bmp.write(b'\x00\x00\x00\x00')

#Image Header
bmp.write(b'x28\x00\x00\x00')
bmp.write(_int32_to_bytes(width))
bmp.write(_int32_to_bytes(height))
bmp.write(b'\x01\x00')
bmp.write(b'\x08\x00')
bmp.write(b'\x00\x00\x00\x00')
bmp.write(b'\x00\x00\x00\x00')
bmp.write(b'\x00\x00\x00\x00')
bmp.write(b'\x00\x00\x00\x00')
bmp.write(b'\x00\x00\x00\x00')
bmp.write(b'\x00\x00\x00\x00')

for c in range(256):
    bmp.write(bytes((c, c, c, 0)))

#Pixel data
pixel_data_bookmark = bmp.tell()
for row in reversed(pixels):
    row_data = bytes(row)
    bmp.write(row_data)
    padding = b'\x00' * ((4 - (len(row)% 4 ))%4)
    bmp.write(padding)

#end of file
eof_bookmark = bmp.tell()

bmp.seek(size_bookmark)
bmp.write(_int32_to_bytes(eof_bookmark))

bmp.seek(pixel_offset_bookmark)
bmp.write(_int32_to_bytes(pixel_data_bookmark))

