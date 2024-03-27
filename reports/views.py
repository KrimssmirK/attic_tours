from django.shortcuts import render
from reports.models import Report, ReportType
from branch.models import Branch
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def stats(request, branch_id):

    selected_branch = Branch.objects.get(pk=branch_id)
    reports = Report.get_current_reports(selected_branch)

    visa_types = ReportType.objects.all()

    context = {
        "branch_id": selected_branch.id,
        "branch_name": selected_branch.name,
        "reports": reports,
        "visa_types": visa_types,
    }

    return render(request, "reports/index.html", context)


class ReportPageView(CreateView):
    model = Report
    template_name = "reports/reports.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("reports:stats", kwargs={"branch_id": self.kwargs["branch_id"]})

    def get_context_data(self, **kwargs):
        context = super(ReportPageView, self).get_context_data(**kwargs)
        branch_id = self.kwargs["branch_id"]
        selected_branch = Branch.objects.get(pk=branch_id)
        context["branch_id"] = selected_branch.id
        context["branch_name"] = selected_branch.name

        return context
