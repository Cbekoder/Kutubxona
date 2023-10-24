from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
def salomlashish(request):
    return HttpResponse("<h1>Assalomu alaykum</h1>")

def homepage(request):
    return render(request, "home.html")

def kitoblar(request):
    soz = request.GET.get("qidirish_sozi")
    natija = Kitob.objects.all()
    if soz:
        natija = natija.filter(nom__contains = soz) or natija.filter(muallif__ism__contains = soz)
    content={
        "kitoblar": natija,
        "mualliflar": Muallif.objects.all(),
        "forma" : KitobForm()
    }
    return render(request, "mashq_uchun/kitoblar.html", content)

def Alisher_Navoiy_kitoblari(request):
    content={
        "kitoblar": Kitob.objects.filter(muallif__ism='Alisher Navoiy')
    }
    return render(request, "mashq_uchun/Alisher_Navoiy_kitoblari.html", content)

def kitob(request, son):
    content = {
        "kitob": Kitob.objects.get(id=son)

    }
    return render(request, "mashq_uchun/kitob.html", content)

def talaba(request):
    if request.method == 'POST':
        # Talaba.objects.create(
        #     ism=request.POST.get("ismi"),
        #     kurs=request.POST.get("k"),
        #     kitob_soni=request.POST.get("k_s")
        # ).save()
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            data = forma.cleaned_data
            Talaba.objects.create(
                ism=data.get("i"),
                kurs=data.get("k"),
                kitob_soni=data.get("k_s")
            ).save()
        return redirect("/talabalar/")
    soz = request.GET.get("qidirish_sozi")
    natija = Talaba.objects.all()
    if soz:
        natija = natija.filter(ism__contains = soz)
    content ={
        "talabalar" : natija,
        "forma": TalabaForm()
    }
    return render(request, "mashq_uchun/talabalar.html", content)

def mualliflar(request):
    if request.method == 'POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            forma.save()
        # Muallif.objects.create(
        #     ism=request.POST.get("ismi"),
        #     jins=request.POST.get("jinsi"),
        #     tugilgan_sana=request.POST.get("t_y"),
        #     kitoblar_soni=request.POST.get("k_s"),
        #     tirik=request.POST.get("t") == "on",
        # ).save()
        return redirect("/mualliflar/")
    soz = request.GET.get("qidirish_sozi")
    content = {
        "mualliflar" : Muallif.objects.all(),
        "forma" : MuallifForm(),
    }
    return render(request, "mashq_uchun/mualliflar.html", content)

def talaba_ochir(request, son):
    Talaba.objects.get(id = son).delete()
    return redirect("/talabalar/")

def muallif_ochir(request, son):
    Muallif.objects.get(id = son).delete()
    return redirect("/mualliflar/")

def kitob_ochir(request, son):
    Kitob.objects.get(id = son).delete()
    return redirect("/kitoblar/")

def talaba_edit(request, pl):
    if request.method == 'POST':
        Talaba.objects.filter(id=pl).update(
            kurs=request.POST.get("k"),
            kitob_soni=request.POST.get("k_s")
        )
        return redirect("/talabalar/")
    content = {
        "talaba" : Talaba.objects.get(id = pl)
    }
    return render(request, 'talaba_update.html', content)
def kitob_edit(request, pl):
    if request.method == 'POST':
        Kitob.objects.filter(id=pl).update(
            janr=request.POST.get("janr"),
            sahifa=request.POST.get("sahifa"),
            muallif=Muallif.objects.get(id=request.POST.get("muallif"))
        )
        return redirect("/kitoblar/")
    content = {
        "kitob" : Kitob.objects.get(id = pl),
        "mualliflar" : Muallif.objects.all(),
        "janrlar" : ["Badiiy", "Ilmiy", "Hujjatli"]
    }
    return render(request, 'kitob_update.html', content)











