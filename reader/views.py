import io

import PyPDF4  #Pure-Python library built as a PDF toolkit

from django.shortcuts import render

from gtts import gTTS #google text-to-speech

from .forms import *

from .langs import *

import pyttsx3  #python text-to-speech

import subprocess

import os

from textReader.settings import BASE_DIR


# Create your views here.


#home page
def home(request):
    context={}
    return render(request,'home.html',context)



#text-to-speech
def textIp(request):
    form=TextFormF()
    if request.method == 'POST':
        form = TextFormF(request.POST)

        mytext = request.POST.get('textType')  #get value of input transcript

        voice = request.POST.get('voices')     #get value of input voice selection.  

        if form.is_valid():
            engine = pyttsx3.init()    #initialize python text-to-speech

            voices = engine.getProperty('voices')  #voice property of python text-to-speech
            if voice =='Female':
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)

            newVoiceRate = 145
            engine.setProperty('rate',newVoiceRate)  #speed property of python text-to-speech

            engine.save_to_file(mytext , 'static/music/test.mp3') #save audio to test.mp3 file
            engine.runAndWait()

            musyc=True
            content={'musyc':musyc}
            return render(request,'text-form.html',content)
            
            
    content={'form':form}
    return render(request,'text-form.html',content)




#pdf-to-speech
def pdfIp(request):
    form=PdfFormF()
    if request.method == 'POST':
        form = PdfFormF(request.POST, request.FILES)
        mypdf = request.FILES['pdfType'].read()   #get value of input pdf

        lang = request.POST.get('language')   #get value of input language selection

        lan=allLang(request,lang)   #function to convert text to gtts language selector.

        if form.is_valid():

            pdfReader=PyPDF4.PdfFileReader(io.BytesIO(mypdf))

            context=""

            context+=pdfReader.getPage(0).extractText()   #extract text from input pdf

            textP=context

            myobj = gTTS(text=textP,lang=lan, slow=False,)  #google text-to-speech create audio of input pdf

            myobj.save("static/music/media.mp3")  #save audio file in media.mp3 file.

            musyc=True
            content={'musyc':musyc}
            return render(request,'pdf-form.html',content)
            
            
    content={'form':form}
    return render(request,'pdf-form.html',content)





#video-editor
def videoIp(request):
    form=VideoFormF()
    if request.method=='POST':
        outPut=os.path.join(BASE_DIR,'static\music\in.mp4') #path of output file to save output
        os.remove(outPut)
        form=VideoFormF(request.POST,request.FILES) 
        if form.is_valid():            
            obj=form.save(commit=False)
            form.save()   #save form input

            inVideo=obj.videoType.path   #get path of input video

            inAudio=obj.audioType.path   #get path of input audio

            #command using ffmpeg for
            # fmpeg to strip the orginial video of its audio
            #ffmpeg to use the new audio and merge it with the video
            #ffmpeg to compress the resultant file and create a low filesize spoken tutorial  
            cmd=f'ffmpeg -i "{inVideo}" -i "{inAudio}" -acodec copy -vcodec copy -map 0:v:0 -map 1:a:0 -b 800k "{outPut}"'

            subprocess.check_output(cmd,shell=True) #subprocess above command
            
            musyc=True
            content={'musyc':musyc}
            return render(request,'video-form.html',content)
            
    content={'form':form}
    return render(request,'video-form.html',content)    
