import matplotlib.pyplot as plt
import numpy as np
#Takes a list of bytes and returns a list of ints which are each
#little-endian groups of 4 bytes
def as_ints(input_bytes):
    if len(input_bytes) % 4 != 0:
        print("Uh oh, might have some trouble")
    int_list = []
    for i in range(0,len(input_bytes),4):
        int_list.append(input_bytes[i] + 256 * (input_bytes[i+1] + 256 *  (input_bytes[i+2] + 256 *  (input_bytes[i+3]))))
    return int_list

with open('PC_COURAGEPOINT_ICON.XBMP','rb') as f:
    filebytes = [int(b) for b in f.read()]
    header = filebytes[:0x20]
    header_ints = as_ints(header)
    total_pixels = header_ints[0]
    image_width = header_ints[2]
    image_data = filebytes[0x20:]
    image_array = []
    pixels = [image_data[i:i+4] for i in range(0,len(image_data),4)]
    print(pixels[7])
    row_count = int(len(pixels) / image_width)
    for i in range(row_count):
        current_row = []
        for j in range(image_width):
            pixel_number = i * image_width + j
            nextpixel = pixels[pixel_number]
            current_row.append(nextpixel)
        image_array.append(current_row)
    plt.imshow(image_array)
    plt.show()
