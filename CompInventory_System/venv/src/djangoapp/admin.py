from django.contrib import admin

# Register your models here.


from .models import Computer
 #it will go into models.py and import computers class
from .forms import ComputerForm
  #it will go into forms.py and import ComputerForm class



class ComputerAdmin(admin.ModelAdmin):
    list_display = ["computer_name","IP_address","MAC_address","users_name","purchase_date", "timestamp"]
    form = ComputerForm
    list_filter = ['computer_name', 'IP_address']
    search_fields = ['computer_name' , 'IP_address','MAC_address']

admin.site.register(Computer,ComputerAdmin)

#and register that class into admin site
