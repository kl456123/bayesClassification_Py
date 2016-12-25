#!/home/breakpoint/anaconda2/bin python
# encoding: utf-8

import imghdr
from os import listdir, remove


def delete_useless_image(path2dir, info=False):

         # set dir
    PATHTODIR = '/home/breakpoint/software/caffe/data/flickr_style/images/'
        for image_name in listdir(PATHTODIR):
            path2image = PATHTODIR + image_name
            #     checkout useless image and
            #     delete it
            #     print(image_name)
                type = imghdr.what(path2image)
                #     print(type)
                    if(type != 'jpeg'):
                        remove(path2image)
                            if(info):
                                print(
                                    '%s image of %s' %
                                    image_name %
                                    type, 'delete success')
