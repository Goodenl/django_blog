from django.views.generic import TemplateView

class ProfilePage(TemplateView):
	template_name = "profiles/profile_page.html"