from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class UpdateProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UpdateProfileForm, self).__init__(*args, **kwargs)
		# self.fields['institute'] = forms.ModelChoiceField(queryset=Institute.objects)
		# self.fields['department'] = forms.ModelChoiceField(queryset=Department.objects)
	class Meta:
		model = Profile
		exclude = []
		widgets = {'user': forms.HiddenInput(),'email': forms.HiddenInput()}

class AdminProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = []

class DisplayProfile(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['user']

class EBForm(forms.ModelForm):
	class Meta:
		model = ExecutiveBoard
		# fields = ('position', 'previous_mun_exp')
		labels = {
			'position': _('Preferred Position'),
			'previous_mun_exp': _('Previous MUNing Experience'),
			'previous_org_com_exp': _('Previous Organising Committee Experience. (If any)'),
			'previous_exe_board_exp': _('Previous Executive Board Experience'),
			'other_exp': _('Other Experience'),
			'slide_position': _("Would you like to be considered for the position of Vice- Chair if the Chair position isn't available?"),
			'ques1': _('What would you do if you are chairing a middle school committee and the committee is drifting from the agenda completely?'),
			'ques2': _('Is there anything that you want us to know?'),
			'file': _('Please attach your Curriculum Vitae')

		}
		exclude = ['user', 'ques3']