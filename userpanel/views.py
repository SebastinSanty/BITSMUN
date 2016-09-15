from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.forms.models import model_to_dict

# Create your views here.

@login_required
def dashboard(request):
	context = {
	}
	return render(request, "dashboard.html", context)

@login_required
def profile(request):
	context = {

	}
	return render(request, "profile.html")

@login_required
def executive_board(request):
	if ExecutiveBoard.objects.filter(user=request.user).count() == 0:
		return redirect('executive_board_reg')
	eb_obj = Profile.objects.get(user=request.user)
	feeddata = model_to_dict(eb_obj)
	print(feeddata.values)
	u1 = EBForm(data=feeddata)
	context = {
		'obj':eb_obj,
		'u' : u1,
	}
	return render(request,"executive_board.html",context)


@login_required
def executive_board_reg(request):
	if request.method == 'POST':

		if ExecutiveBoard.objects.filter(user=request.user).count() == 0:
			form = EBForm(request.POST, request.FILES,initial={'user': request.user.id})
		else:
			eb_obj = ExecutiveBoard.objects.get(user=request.user)
			form = EBForm(request.POST,request.FILES, instance=eb_obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('executive_board')
	else:
		if ExecutiveBoard.objects.filter(user=request.user).count() == 0:
			form = EBForm(initial={'user': request.user.id})
		else:
			eb_obj = ExecutiveBoard.objects.get(user=request.user)
			form = EBForm(instance=eb_obj)
	context = {
		'form' : form
	}
	return render(request, "executive_board_reg.html", context)

@login_required
def delegates(request):
	context = {

	}
	return render(request, "delegates.html", context)

@login_required
def press_members(request):
	context = {

	}
	return render(request, "press_members.html", context)


@login_required
def SeeProfile(request):
	if Profile.objects.filter(user=request.user).count() == 0:
		return redirect('fillprofile')
		print("Hello")
	profile_obj = Profile.objects.get(user=request.user)
	feeddata = model_to_dict(profile_obj)
	print(feeddata.values)
	u1 = DisplayProfile(data=feeddata)
	context = {
		'obj':profile_obj,
		'u' : u1,
	}
	return render(request,"profile.html",context)

# @login_required
# def UpdateProfile(request):
# 	profile_obj = Profile.objects.get(username=request.user)
# 	form = UpdateProfileForm(request.POST or None, instance=profile_obj)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('profile')
		
# 	context = {
# 		'form' : form
# 	}
# 	return render(request,"updateprofile.html",context)

@login_required
def FillProfile(request):
	if request.method == 'POST':

		if Profile.objects.filter(user=request.user).count() == 0:
			form = UpdateProfileForm(request.POST, request.FILES,initial={'user': request.user.id,'email':User.objects.get(username=request.user.username).email})
		else:
			profile_obj = Profile.objects.get(user=request.user)
			form = UpdateProfileForm(request.POST,request.FILES, instance=profile_obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.email = User.objects.get(username=request.user.username).email
			instance.save()
			return redirect('profile')
	else:
		if Profile.objects.filter(user=request.user).count() == 0:
			form = UpdateProfileForm(initial={'user': request.user.id,'email':User.objects.get(username=request.user.username).email})
		else:
			profile_obj = Profile.objects.get(user=request.user)
			form = UpdateProfileForm(instance=profile_obj)
	context = {
		'form' : form
	}
	
	return render(request,"updateprofile.html",context)