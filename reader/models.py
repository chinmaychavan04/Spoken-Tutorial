from django.db import models

#list languages
language_list=sorted({
    ('English','English'),('Hindi','Hindi'),('German','German'),
    ('Marathi','Marathi')
})


#list for differt voice
voice_list=sorted({
    ('Male','Male'),('Female','Female')
})

# Create your models here.


# text-to-speech model
class TextForm(models.Model):
    textType=models.TextField(max_length=5000,null=True)
    voices=models.CharField(max_length=50,choices=voice_list)
    
    def __str__(self):
        return str(self.id)


#pdf-to-speech model
class PdfForm(models.Model):
    pdfType=models.FileField(upload_to="pdfs")
    language=models.CharField(max_length=50,choices=language_list)
    
    def __str__(self):
        return str(self.id)        



#video-to-speech model
class VideoForm(models.Model):
    videoType=models.FileField(upload_to="videos")
    audioType=models.FileField(upload_to="audios")
    
    def __str__(self):
        return str(self.id)         