from io import BufferedReader

def get_image(f: BufferedReader):
    assert f.readline().strip() == b"P6", "Not P6 ppm"
    W, H = map(int, f.readline().strip().split())
    assert f.readline().strip() == b"255", "Color range is not 255"
    byte_length = 1

    ## TODOs
    img = []
    for i in range(W):
        row = []
        for j in range(H):
            r_byte= f.read(byte_length)
            g_byte= f.read(byte_length)
            b_byte= f.read(byte_length)
            r = int.from_bytes(r_byte,byteorder='big')
            g = int.from_bytes(g_byte,byteorder='big')
            b = int.from_bytes(b_byte,byteorder='big')
            # if i < 2:
                # print(r,g,b)
            row.append([r, g, b])
        img.append(row)

    return img


if __name__ == "__main__":
    import numpy as np

    input_filename = "img.ppm"
    with open(input_filename, "rb") as f:
        img_matrix = np.array(get_image(f), dtype=np.uint8)
        assert img_matrix.shape == (794, 1265, 3)
        assert img_matrix.max() <= 255 and img_matrix.min() >= 0, "Out of Bound"
    with open("part_mws.bin", "rb") as f:
        mws_bytes = f.read()
    output_filename = "img_full.ppm"
    with open(output_filename, "wb") as f:
        f.write(b"P6\n")
        f.write(b"794 1621\n")
        f.write(b"255\n")
        f.write(img_matrix.tobytes())
        f.write(mws_bytes)
