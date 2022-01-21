from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TweetModel

# Register your models here.
admin.site.register(TweetModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다