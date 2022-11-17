# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 08:21:44 2022

@author: Demiso
"""
#use this to download data from ftp

from ftplib import FTP
import os, sys, os.path

#progressbar import statements
import progressbar
from progressbar import Bar, ETA, FileTransferSpeed, Percentage, ProgressBar
widgets = ['Downloading: ', Percentage(), ' ',
                    Bar(marker='#',left='[',right=']'),
                    ' ', ETA(), ' ', FileTransferSpeed()]

def downloadChirps(directory,filename,local_folder=None):
    
    #Connecting to the ftp server
    ftp = FTP('ftp.chc.ucsb.edu')
    ftp.login()
    #Changing to the given directory
    print ('Changing to ' + directory)
    try:
        ftp.cwd(directory)
    except:
        print('The given directory does not exist. Please provide a valid Chirps ftp directory, under which there is the file with the given filename.')
        ftp.close()
        return

    #Setting up local file, requesting (and downloading) file from server, and writing it to local file.
    if local_folder == None:
        print('No local folder given. The file will be saved in your current working drectory.')
        local_filename = filename
    else:
        local_filename = os.path.join(local_folder, filename)
    size = ftp.size(filename)
    file = open(local_filename, 'wb')
    
    print('Starting to download file. This might take a while...')
    pbar = progressbar.ProgressBar(widgets=widgets, maxval=size)
    pbar.start()

    def file_write(data):
       file.write(data) 
       global pbar
       pbar += len(data)
    
    ftp.retrbinary("RETR " + filename, file_write)    
    file.close()
    print('Download finished. File saved as '+local_filename+'.')
    ftp.quit()