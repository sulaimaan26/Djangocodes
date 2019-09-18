from django.shortcuts import render
from . models import Header,HomepageBanner,HomepageDestination,HomepageOffersection,HomepageVideo,HomepagePopularDestionation,HomepageSpecialOffers
from django.conf import settings

from filemanager import FileManager
# Create your views here.

def index(request):
    classact=Header.objects.values('header_menu').filter(id=1)
    headvar=Header.objects.all()
    banner=HomepageBanner.objects.all()
    Homepagedestination=HomepageDestination.objects.all()
    HomepageDestinationtop=HomepageDestination.objects.values('Destination_Title','Destination_Message').filter(id=1)
    Homepageoffersection=HomepageOffersection.objects.all()
    Homepagevideo=HomepageVideo.objects.all()
    HomepagepopularDestionation=HomepagePopularDestionation.objects.all()
    popularDestionationtop=HomepagePopularDestionation.objects.values('Title','Description').filter(id=1)
    specialoffer=HomepageSpecialOffers.objects.all()
    specialoffertop=HomepageSpecialOffers.objects.values('Title','Description').filter(id=1)
    return render(request,'index.html',{'header':headvar,'classact':classact.get(),'banner':banner.get(),'destination':Homepagedestination,
    'destinationtitle':HomepageDestinationtop.get(),'offer':Homepageoffersection.get(),'video':Homepagevideo.get(),'popdestination':HomepagepopularDestionation
    ,'poptit':popularDestionationtop.get(),'specoffertop':specialoffertop.get(),'specoffer':specialoffer
    })



def view(request, path):
    extensions = ['html', 'htm', 'zip', 'py', 'css', 'js', 'jpeg', 'jpg', 'png']
    fm = FileManager(settings.MEDIA_ROOT, extensions=extensions)
    return fm.render(request, path)


