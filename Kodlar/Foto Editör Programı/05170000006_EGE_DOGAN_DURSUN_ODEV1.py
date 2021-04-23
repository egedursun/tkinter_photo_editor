 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EGE DOĞAN DURSUN
05170000006
EGE ÜNİVERSİTESİ
MÜHENDİSLİK FAKÜLTESİ
BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
2020-2021 ÖĞRETİM YILI / GÜZ DÖNEMİ

GÖRÜNTÜ İŞLEME DERSİ
PROJE - 1
"""

#Import necessary libraries
import scipy
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFilter, ImageOps, ImageEnhance
from skimage.transform import swirl
from skimage import *
from skimage import morphology
import copy
import numpy as np
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

#Create a window for the application and set the default resolution
window = Tk()
window.title("ABODE PHOTOSHOCK V1.0")
window.geometry("1800x1200")


#LOAD IMAGE
def btn_load_clicked():
   FILE = filedialog.askopenfilename(initialdir="/", title="Select Image", 
                                         filetypes=(("jpeg files","*.jpg"),)) 
   
   img = Image.open(FILE)
   global IMAGE
   IMAGE = copy.deepcopy(img)
   print(IMAGE)
   w, h = img.size
   img = img.resize((750, int(750*h/w)), Image.ANTIALIAS)
   img = ImageTk.PhotoImage(img)
   global panel
   panel = Label(window, image=img)
   panel.image = img
   panel.place(x=800, y=550, anchor="center")
   
   
#SAVE IMAGE
def btn_save_clicked():
    
    FILE = filedialog.asksaveasfilename(initialdir="/", title="Save File",
                                        filetypes=(("jpeg files", "*.jpg"),))
    
    global IMAGE
    IMAGE.save(FILE)
    

#FILTER NUMBER 1 : BLUR
def btn_filter_blur():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.BLUR)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 2 : CONTOUR
def btn_filter_contour():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.CONTOUR)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 3 : DETAIL
def btn_filter_detail():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.DETAIL)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 4 : EDGE ENHANCE
def btn_filter_edge_enhance():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.EDGE_ENHANCE)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 5 : EDGE ENHANCE MORE
def btn_filter_edge_enhance_more():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.EDGE_ENHANCE_MORE)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 6 : EMBOSS
def btn_filter_emboss():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.EMBOSS)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 7 : FIND EDGES
def btn_filter_find_edges():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.FIND_EDGES)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 8 : SHARPEN
def btn_filter_sharpen():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.SHARPEN)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 9 : SMOOTH
def btn_filter_smooth():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.SMOOTH)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FILTER NUMBER 10 : SMOOTH MORE
def btn_filter_smooth_more():
    
    global IMAGE
    image = IMAGE.filter(ImageFilter.SMOOTH_MORE)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
#ROTATE LEFT (WITHOUT EXPANSION)
def btn_rotate_left():
    
    global IMAGE
    image = IMAGE.rotate(90)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#ROTATE RIGHT (WITHOUT EXPANSION)
def btn_rotate_right():
    
    global IMAGE
    image = IMAGE.rotate(-90)
    w, h = image.size
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#FLIP IMAGE HORIZONTALLY
def btn_flip_hor():
    
    global IMAGE
    image = IMAGE.transpose(Image.FLIP_LEFT_RIGHT)
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#FLIP IMAGE VERTICALLY
def btn_flip_ver():
    
    global IMAGE
    image = IMAGE.transpose(Image.FLIP_TOP_BOTTOM)
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#SHOW HISTOGRAM
class MyDialog3:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='HISTOGRAM ')
        self.myLabel.pack()
        
        global hist
        self.imageLabel = Label(top, image=hist)
        self.imageLabel.pack()
        self.imageLabel.image = hist
        self.imageLabel.pack()


    def send(self):
        self.top.destroy()
        
def btn_show_histogram():
    
    global IMAGE
    img = img_as_float(IMAGE)
    
    histogram, bin_edges = np.histogram(img, bins=256, range=(0, 1))
    
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixels")
    plt.xlim([0.0, 1.0]) 
    
    plt.plot(bin_edges[0:-1], histogram)  
    plt.savefig("histogram-img.png")
    
    global hist
    hist = Image.open("histogram-img.png")
    w, h = hist.size
    hist = hist.resize((750, int(750*h/w)), Image.ANTIALIAS)
    hist = ImageTk.PhotoImage(hist)
    
    inputDialog = MyDialog3(window)
    window.wait_window(inputDialog.top)
    
#EQUALIZE IMAGE
def btn_equalize():
    global IMAGE
    image = ImageOps.equalize(IMAGE, mask = None) 
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#RESCALE INTENSITY 
class MyDialog2:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='Enter New Intensity/Gamma Value : ')
        self.myLabel.pack()

        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()

        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        global intensity
        intensity = self.myEntryBox.get()
        self.top.destroy()

        
def btn_rescale_intensity():
    
    inputDialog = MyDialog2(window)
    window.wait_window(inputDialog.top)
    
    global IMAGE
    img = img_as_float(IMAGE)
    gamma_corrected = exposure.adjust_gamma(img, int(intensity))
    image = Image.fromarray(np.uint8(gamma_corrected*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
#RESIZE
class MyDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='Enter New Width : ')
        self.myLabel.pack()

        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()
        
        self.myLabel2 = Label(top, text="Enter New Height : ")
        self.myLabel2.pack()
        
        self.myEntryBox2 = Entry(top)
        self.myEntryBox2.pack()

        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        global width
        width = self.myEntryBox.get()
        global height
        height = self.myEntryBox2.get()
        self.top.destroy()
        
def btn_resize():
    
    inputDialog = MyDialog(window)
    window.wait_window(inputDialog.top)
    
    global IMAGE
    image = IMAGE.resize((int(width), int(height)), Image.ANTIALIAS)
    
    IMAGE = image
    
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image="")
    panel.image = image
    panel.configure(image=image)
    panel.place(x=800, y=550, anchor="center")
    

#CROP
class MyDialog4:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='From Top : ')
        self.myLabel.pack()

        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()
        
        self.myLabel2 = Label(top, text="From Left : ")
        self.myLabel2.pack()
        
        self.myEntryBox2 = Entry(top)
        self.myEntryBox2.pack()
        
        self.myLabel3 = Label(top, text="From Bottom : ")
        self.myLabel3.pack()
        
        self.myEntryBox3 = Entry(top)
        self.myEntryBox3.pack()
        
        self.myLabel4 = Label(top, text="From Right : ")
        self.myLabel4.pack()
        
        self.myEntryBox4 = Entry(top)
        self.myEntryBox4.pack()

        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        global topp
        topp = self.myEntryBox.get()
        global left
        left = self.myEntryBox2.get()
        global bottom
        bottom = self.myEntryBox3.get()
        global right
        right = self.myEntryBox4.get()
        self.top.destroy()
        
def btn_crop():
    
    inputDialog = MyDialog4(window)
    window.wait_window(inputDialog.top)     
    
    global IMAGE
    wI, hI = IMAGE.size  
    image = IMAGE.crop((int(left), int(topp), wI-int(right), hI-int(bottom)))
    
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")

    
    
#SWIRL
def btn_swirl():
    
    global IMAGE
    img = img_as_float(IMAGE)
    swirled = swirl(img, rotation=0, strength=10, radius=120)
    
    image = Image.fromarray(np.uint8(swirled*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")

    
#SUPER FILTER
def btn_super_filter():
    global IMAGE
    #change brightness
    br_enh = ImageEnhance.Brightness(IMAGE)
    image = br_enh.enhance(0.8)
    #change contrast
    cnt_enh = ImageEnhance.Contrast(image)
    image = cnt_enh.enhance(1.5)
    #change sharpness
    shrp_enh = ImageEnhance.Sharpness(image)
    image = shrp_enh.enhance(1.4)
    #change color
    clr_enh = ImageEnhance.Color(image)
    image = clr_enh.enhance(1.8)
    #apply blur
    image = image.filter(ImageFilter.BLUR)
    
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
#ACTIVE CONTOUR
def btn_active_contour():
    """
    global IMAGE
    
    img = img_as_float(IMAGE)
    """
    
    split_version = scipy.__version__.split('.')
    if not(split_version[-1].isdigit()): 
            split_version.pop()
    scipy_version = list(map(int, split_version))
    new_scipy = scipy_version[0] > 0 or \
                (scipy_version[0] == 0 and scipy_version[1] >= 14)
    
    img = data.astronaut()
    img = rgb2gray(img)
    
    s = np.linspace(0, 2*np.pi, 400)
    x = 220 + 100*np.cos(s)
    y = 100 + 100*np.sin(s)
    init = np.array([x, y]).T
    
    if not new_scipy:
        print('Old version!')
    
    if new_scipy:
        snake = active_contour(gaussian(img, 3),
                               init, alpha=0.015, beta=50, gamma=0.001)

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111)
    plt.gray()
    ax.imshow(img)
    ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
    ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, img.shape[1], img.shape[0], 0])

    plt.savefig("active_contour.png")
    
    img = Image.open("active_contour.png")
    w, h = img.size
    img = img.resize((750, int(750*h/w)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel = Label(window, image=img)
    panel.image = img
    panel.place(x=800, y=550, anchor="center")
    
#MORPHOLOGY 1 : BLACK TOP HAT
def btn_morph_black_tophat():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.black_tophat(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#MORPHOLOGY 2 : LOCAL MAXIMA
def btn_morph_local_maxima():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.local_maxima(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#MORPHOLOGY 3 : LOCAL MINIMA
def btn_morph_local_minima():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.local_minima(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    

#MORPHOLOGY 4 : WHITE TOPHAT
def btn_morph_white_tophat():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.white_tophat(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#MORPHOLOGY 5 : BINARY EROSION
def btn_morph_binary_erosion():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.binary_erosion(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#MORPHOLOGY 6 : BINARY OPENING
def btn_morph_binary_opening():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.binary_opening(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#MORPHOLOGY 7 : BINARY DILATION
def btn_morph_binary_dilation():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.binary_dilation(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#MORPHOLOGY 8 : BINARY CLOSING
def btn_morph_binary_closing():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.binary_closing(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#MORPHOLOGY 9 : WATERSHED
def btn_morph_watershed():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.watershed(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")
    
    
#MORPHOLOGY 10 : DILATION
def btn_morph_dilation():
    global IMAGE
    img = img_as_float(IMAGE)
    img = morphology.dilation(img)
    image = Image.fromarray(np.uint8(img*255))
    w, h = image.size                       
    IMAGE = image
    image = image.resize((750, int(750*h/w)), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    global panel
    panel = Label(window, image=image)
    panel.image = image
    panel.place(x=800, y=550, anchor="center")

#create the buttons inside the application and link them to the adequate button event method
btn_load = Button(window, text="LOAD IMAGE", width=10, height=3, command=btn_load_clicked)
btn_save = Button(window, text="SAVE IMAGE", width=12, height=3, command=btn_save_clicked)
btn_fl1 = Button(window, text="BLUR", width=18, height=3, command=btn_filter_blur)
btn_fl2 = Button(window, text="CONTOUR", width=15, height=3, command=btn_filter_contour)
btn_fl3 = Button(window, text="DETAIL", width=6, height=3, command=btn_filter_detail)
btn_fl4 = Button(window, text="EDGE ENHANCE", width=12, height=3, command=btn_filter_edge_enhance)
btn_fl5 = Button(window, text="EDGE ENHANCE MORE", width=16, height=3, command=btn_filter_edge_enhance_more)
btn_fl6 = Button(window, text="EMBOSS", width=13, height=3, command=btn_filter_emboss)
btn_fl7 = Button(window, text="FIND EDGES", width=15, height=3, command=btn_filter_find_edges)
btn_fl8 = Button(window, text="SHARPEN", width=7, height=3, command=btn_filter_sharpen)
btn_fl9 = Button(window, text="SMOOTH", width=7, height=3, command=btn_filter_smooth)
btn_fl10 = Button(window, text="SMOOTH MORE", width=12, height=3, command=btn_filter_smooth_more)
btn_hist = Button(window, text="SHOW HISTOGRAM", width=15, height=3, command=btn_show_histogram)
btn_equ = Button(window, text="EQUALIZE", width=7, height=3, command=btn_equalize)
btn_rot_l = Button(window, text="ROTATE LEFT", width=10, height=3, command=btn_rotate_left)
btn_rot_r = Button(window, text="ROTATE RIGHT", width=12, height=3, command=btn_rotate_right)
btn_inv_h = Button(window, text="FLIP HORIZONTALLY", width=18, height=3, command=btn_flip_hor)
btn_inv_v = Button(window, text="FLIP VERTICALLY", width=15, height=3, command=btn_flip_ver)
btn_swrl = Button(window, text="SWIRL", width=6, height=3, command=btn_swirl)
btn_resize = Button(window, text="RESIZE", width=12, height=3, command=btn_resize)
btn_crop = Button(window, text="CROP", width=16, height=3, command=btn_crop)
btn_active_cont = Button(window, text="ACTIVE CONTOUR", width=13, height=3, command=btn_active_contour)
btn_rsc_int = Button(window, text="RESCALE INTENSITY", width=15, height=3, command=btn_rescale_intensity)
btn_mp1 = Button(window, text="BLACKTOPHAT", width=10, height=3, command=btn_morph_black_tophat)
btn_mp2 = Button(window, text="LOCAL MAXIMA", width=12, height=3, command=btn_morph_local_maxima)
btn_mp3 = Button(window, text="LOCAL MINIMA", width=18, height=3, command=btn_morph_local_minima)
btn_mp4 = Button(window, text="WHITE TOPHAT", width=15, height=3, command=btn_morph_white_tophat)
btn_mp5 = Button(window, text="EROSION", width=6, height=3, command=btn_morph_binary_erosion)
btn_mp6 = Button(window, text="BINARY OPENING", width=12, height=3, command=btn_morph_binary_opening)
btn_mp7 = Button(window, text="BINARY DILATION", width=16, height=3, command=btn_morph_binary_dilation)
btn_mp8 = Button(window, text="BINARY CLOSING", width=13, height=3, command=btn_morph_binary_closing)
btn_mp9 = Button(window, text="WATERSHED", width=15, height=3, command=btn_morph_watershed)
btn_mp10 = Button(window, text="DILATION", width=7, height=3, command=btn_morph_dilation)
btn_super_flt = Button(window, text="SUPER FILTER", width=15, height=3, command=btn_super_filter)

#design grids for button positions inside the application
btn_load.grid(column=0, row=0)
btn_save.grid(column=1, row=0)
btn_fl1.grid(column=2, row=0)
btn_fl2.grid(column=3, row=0)
btn_fl3.grid(column=4, row=0)
btn_fl4.grid(column=5, row=0)
btn_fl5.grid(column=6, row=0)
btn_fl6.grid(column=7, row=0)
btn_fl7.grid(column=8, row=0)
btn_fl8.grid(column=9, row=0)
btn_fl9.grid(column=10, row=0)
btn_fl10.grid(column=11, row=0)
btn_hist.grid(column=12, row=0)
btn_equ.grid(column=13, row=0)
btn_rsc_int.grid(column=14, row=0)

btn_rot_l.grid(column=0, row=1)
btn_rot_r.grid(column=1, row=1)
btn_inv_h.grid(column=2, row=1)
btn_inv_v.grid(column=3, row=1)
btn_swrl.grid(column=4, row=1)
btn_resize.grid(column=5, row=1)
btn_crop.grid(column=6, row=1)
btn_active_cont.grid(column=7, row=1)
btn_super_flt.grid(column=8, row=1)

btn_mp1.grid(column=0, row=2)
btn_mp2.grid(column=1, row=2)
btn_mp3.grid(column=2, row=2)
btn_mp4.grid(column=3, row=2)
btn_mp5.grid(column=4, row=2)
btn_mp6.grid(column=5, row=2)
btn_mp7.grid(column=6, row=2)
btn_mp8.grid(column=7, row=2)
btn_mp9.grid(column=8, row=2)
btn_mp10.grid(column=9, row=2)


window.mainloop()