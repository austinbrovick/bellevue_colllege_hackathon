from django.shortcuts import render, redirect
from .models import Tag
from .forms import SearchTagForm
from clubs.models import Club
from django.http.response import HttpResponse
from profiles.models import Profile



def find_tags(request):

    form = SearchTagForm(request.POST)
    if form.is_valid():
        search = form.cleaned_data['search']
        club, created = Club.objects.get_or_create(president=request.user)
        searched_tags = Tag.objects.filter(name__icontains=search)
        tags = Tag.objects.filter(club=club)
        print(tags)
    else:
        return redirect('my_club')


    connections = []
    profiles = Profile.objects.all()

    for tag_from_club in tags:
        for profile in profiles:
            for tag_from_user in profile.tags.all():
                if tag_from_user.name == tag_from_club.name:
                    connections.append(profile)

    print(connections)
    unique_connections = []

    for x in connections:
        status = True
        for y in unique_connections:
            if x == y:
                status = False
        if status == True:
            unique_connections.append(x)

    print(unique_connections)



    return render(request, "club/club.html", {"club": club, "form":SearchTagForm(), 'tags':tags, 'connections':unique_connections, 'searched_tags':searched_tags,})

    # return render(request, "club/club.html", {"club": club, "form":SearchTagForm(), 'searched_tags':searched_tags, 'tags':tags})

def add_tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    club = Club.objects.get(president=request.user)
    club.tags.add(tag)
    club.save()
    print(tag)
    return redirect('my_club')
    # return HttpResponse("hello")


def add_tag_profile(request, pk):
    tag = Tag.objects.get(pk=pk)
    profile = Profile.objects.get(user=request.user)
    profile.tags.add(tag)
    profile.save()
    return redirect('profile')



def find_tags_profile(request):
    form = SearchTagForm(request.POST)
    if form.is_valid():
        search = form.cleaned_data['search']
        # club, created = Club.objects.get_or_create(president=request.user)
        searched_tags = Tag.objects.filter(name__icontains=search)
        tags = Tag.objects.filter(profile=request.user.profile)
        print(tags)
        return render(request, "profiles/my_profile.html", {"my_profile": request.user, "form":SearchTagForm(), 'searched_tags':searched_tags, 'tags':tags})
    else:
        return redirect('my_club')

