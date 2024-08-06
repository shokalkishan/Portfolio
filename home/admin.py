from django.contrib import admin

from .models import Projects 
from .models import Education
from .models import Profile
from .models import Skill
from .models import Soft_Skill
from .models import Experience
from .models import Team
from .models import Contact
from .models import Coding_profile
# Register your models here.



admin.site.register(Projects)
admin.site.register(Education)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Soft_Skill)
admin.site.register(Experience)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Coding_profile)