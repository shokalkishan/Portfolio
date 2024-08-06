from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.contrib import messages
from .models import Projects 
from .models import Education
from .models import Profile
from .models import Skill
from .models import Soft_Skill
from .models import Experience
from .models import Team
from .models import Contact
from .models import Coding_profile
import random
# Create your views here.
import logging

# Create a logger
logger = logging.getLogger(__name__)

# Log a message


def index(request):
    projects=Projects.objects.all()
    education=Education.objects.all()
    profile=Profile.objects.all()
    skill=Skill.objects.all()
    soft_skill=Soft_Skill.objects.all()
    experience=Experience.objects.all()
    coding_profile=Coding_profile.objects.all()
    coding_profile_color=["#483d8b","#d2691e","	#008b8b","#8b008b","#8b0000","#9400d3","#b22222"]
    random.shuffle(coding_profile_color)
    profile_color=[]
    for i in range(len(coding_profile)):
        profile_color.append([coding_profile[i],coding_profile_color[i]])
    params={"n_pro":len(projects),"range":range(len(projects)),
            "projects":projects,"education":education,"profile":profile,
            "skill":skill,"soft_skill":soft_skill,"experience":experience,
            "profile_color":profile_color
            }

    return render(request,"index.html",params)

def project_details(request,name):
    project=get_object_or_404(Projects,name=name)
    # project=Projects.objects.(id=project_id)
    params={"project":project}
    desc=project.desc 
    description_list=desc.split('.')
    profile=Profile.objects.all()
    if(len(description_list[len(description_list)-1])==0):
        description_list.pop()
    team_obj=Team.objects.filter(project_id=name)
    team=[]

    for ob in team_obj:
        tm=Profile.objects.get(email=ob.member_id.email)
        team.append(tm)
        print(ob.member_id,ob.project_id,ob.member_id.email)
    params={
        "project":project,
        "desc":description_list,
        "team":team,
        "profile":profile
        }

    return render(request,"project_details.html",params)

def experience_details(request,name):
    experience=get_object_or_404(Experience,title=name)
    profile=Profile.objects.all()
    description_list=experience.desc.split('.')
    
    if(len(description_list[len(description_list)-1])==0):
        description_list.pop()
    params={
        "experience":experience,
        "desc":description_list,
        "profile":profile

    }
    return render(request,"experience.html",params)

def contact(request):
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    message=request.POST['message']
    query=Contact.objects.create(name=name,email=email,subject=subject,message=message)
    query.save()
    previous_url = request.META.get('HTTP_REFERER')
    messages.success(request, 'Success message.')
    return redirect(previous_url)