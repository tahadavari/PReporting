from django.shortcuts import render, redirect

from report.forms.report_form import ReportForm
from report.models import Report


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            report = Report.objects.create(
                operator_name=clean_data['operator_name'],
                start_time=clean_data['start_time'],
                end_time=clean_data['end_time'],
                production_piece_count=clean_data['production_piece_count'],
                defective_piece_count=clean_data['defective_piece_count'],
                machine=clean_data['machine'],
                report_text=clean_data['report_text'],
            )
            print(report)
            form = ReportForm()
            context = {
                'form': form
            }
            return render(request, 'report_form.html', context)
    if request.user.is_authenticated:
        form = ReportForm()
        context = {
            'form': form
        }
        return render(request, 'report_form.html', context)
    else:
        return redirect('login')
