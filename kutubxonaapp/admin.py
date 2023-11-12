from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ['id', "ism", "tugilgan_sana", 'tirik', 'kitoblar_soni']
    list_display_links = ['id', 'ism']
    list_editable = ["tirik"]
    search_fields = ["ism", 'id', 'tugilgan_sana']
    search_help_text = "Id, ism va tug'ilgan yillari bo'yicha qidiring!"
    list_filter = ['tirik']
    ordering = ['ism']
    date_hierarchy = 'tugilgan_sana'
    list_per_page = 10

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'sahifa', 'janr', 'muallif']
    list_display_links = ['id', 'nom']
    search_fields = ['id', 'nom', 'janr', 'muallif__ism']
    search_help_text = 'Id, nom, janr va muallif bo\'yicha qidiring!'
    list_editable = ['sahifa']
    list_filter = ['janr', 'muallif__ism']
    autocomplete_fields = ['muallif']


admin.site.register(Talaba)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
admin.site.register(Kutubxonachi)
admin.site.register(Record)

# admin.site.unregister(Group)
# admin.site.unregister(User)
