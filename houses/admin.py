from django.contrib import admin
from .models import House

# Register your models here.


@admin.register(House)  # 아래 클래스는 하우스 모델을 컨트롤하는 클래스다
class HouseAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_night", "address", "pet_allowed")

    list_filter = ("price_per_night", "pet_allowed")
