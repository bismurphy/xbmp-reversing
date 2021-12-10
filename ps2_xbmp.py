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
def show_colortable(table):
    image_array = []
    for i in range(0,len(colortable),16):
        row = table[i:i+16]
        builtup_row = []
        for x in row:
            r,g,b,a = x
            builtup_row.append([r,g,b,a])
        image_array.append(builtup_row)
    plt.imshow(image_array)
    plt.show()
with open('PS2_COURAGEPOINTS_ICON.XBMP','rb') as f:
    filebytes = [int(b) for b in f.read()]
    header = filebytes[:0x20]
    header_ints = as_ints(header)
    total_pixels = header_ints[0]
    image_width = header_ints[2]
    colortable_start = 0x20 + total_pixels
    indexed_image = filebytes[0x20:colortable_start]
    colortable_bytes = filebytes[colortable_start:]
    colortable = [colortable_bytes[i*4:i*4+3]+[colortable_bytes[i*4+3]*2] for i in range(256)]
    #colortable = [colortable_bytes[i*4:i*4+4] for i in range(256)]
    show_colortable(colortable)
    
    image_array = []
    for i in range(0,len(indexed_image),image_width):
        row = indexed_image[i:i+image_width]
        builtup_row = []
        for x in range(len(row)):
            r,g,b,a = colortable[min(row[x],255)]
            builtup_row.append([r,g,b,a])
        image_array.append(builtup_row)

    np_colortable = np.array(colortable)
    square_colortable = np_colortable.reshape((16,16,4))
    plt.imshow(image_array)
    plt.show()
