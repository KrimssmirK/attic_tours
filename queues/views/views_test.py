from django.shortcuts import render

# this is just for draft design purpose (HTML and CSS)
def test_view(request):
    template_path = "queues/applicant/test.html"
    context = {}
    return render(request, template_path, context)
