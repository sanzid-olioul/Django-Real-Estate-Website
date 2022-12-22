from .models import AllSocialLink
def add_footer_variable_to_context(request):
        links = AllSocialLink.objects.all()
        if links:
            links = links[0]
            return{
                'facebook':links.facebook,
                'twitter': links.twitter,
                'instagram': links.instagram,
                'linkedin': links.linkedin,
                'mail': links.mail,
                'phone': links.phone,
                'about': links.about,
                'name':links.company_name
            }

        else:
            return dict()