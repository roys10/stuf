import numpy as np
from matplotlib import image as mpimg


def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


def compress(path):
    img = mpimg.imread(rf'{path}')
    gray_img = rgb2gray(img)
    comped = []
    for i in gray_img:
        # print(pd.Series(i).value_counts())
        tmp = []

        for j in i:
            value = j
            counter = np.count_nonzero(i == value)
            if not (f"{value}*{counter}" in tmp):
                tmp.append(f"{value}*{counter}")

            # if counter == 1: this is in order to save values which their counter is 1 without the *1
            #     tmp.append(f"{value}")
            # else:
            #     tmp.append(f"{value}*{counter}")
            # print(i, counter)
        comped.append(tmp)
    return comped

def main():
    end = compress(r"C:\Users\royse\OneDrive\תמונות\bruh.jpg")
    print(end)



if __name__ == "__main__":
    main()











# img = mpimg.imread(r'C:\Users\royse\OneDrive\תמונות\bruh.jpg')
# #m = np.array(np.array([[1, 2, 2], [3, 3, 4]]))
# #m = list(m)
# #print(m)

# m = rgb2gray(img)
# print(m)
# compress([[230, 230, 50], [50, ]])
# comped = []
# for i in m:
#     # print(pd.Series(i).value_counts())
#     tmp = []
#
#     for j in i:
#         value = j
#         counter = np.count_nonzero(i == value)
#         if not (f"{value}*{counter}" in tmp):
#             tmp.append(f"{value}*{counter}")
#         #print(i, counter)
#     comped.append(tmp)
# print(comped)
