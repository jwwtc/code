from glob import glob
import cv2
import os

#img_mask = r'C:\Users\mikep\Desktop\project\images\*.tif'

in_dir = r'C:\Users\mikep\Desktop\project\images'
out_dir = r'C:\Users\mikep\Desktop\1212'

infiles = in_dir + '\*1.png'
img_names = glob(infiles)
print(img_names)

for fn in img_names:
    print('processing %s...' % fn,)
    im_gray = cv2.imread(fn, 0)
    thresh = 0
    im_bw = cv2.threshold(im_gray, thresh, 0, cv2.THRESH_BINARY)[1]
    #im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    name = os.path.basename(fn)
    outfile = out_dir + '/' + name
    cv2.imwrite(outfile, im_gray)
    print('END')



