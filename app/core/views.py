import logging

from django.db.models import Sum
from django.shortcuts import redirect
from django.views.generic import FormView, ListView, DetailView

from core.forms import XLSUploadForm
from core.models import UploadedFile


logger = logging.getLogger(__name__)


class FileUploadView(FormView):
    """
    Main page view. Using the file uploading and parsing form
    """
    form_class = XLSUploadForm
    template_name = 'core/upload_form.html'

    def form_valid(self, form):
        """
        Tries to save parsed data from the file.
        In case of an exception provides an explanation to the user
        :param form: form object
        :return: response that redirects user to parsing result or reloads page showing all error messages
        """
        try:
            file = form.save()
        except Exception as e:
            form.add_error('file', e)
            return self.form_invalid(form)
        return redirect('detail', file.pk)


class UploadHistoryListView(ListView):
    """
    Uploads history page
    """
    model = UploadedFile
    template_name = 'core/upload_history.html'


class UploadedFileDetailView(DetailView):
    """
    Parsed data detail view
    """
    model = UploadedFile
    template_name = 'core/file_detail.html'

    def get_context_data(self, **kwargs):
        """
        Extension for Django's default view context collector.
        Here is where all the statistics logic implemented
        :return: context dict
        """
        context = super(UploadedFileDetailView, self).get_context_data(**kwargs)
        group_fields = ['date']
        data_fields = [
            'fact_qliq_data1', 'fact_qliq_data2', 'fact_qoil_data1', 'fact_qoil_data2',
            'forecast_qliq_data1', 'forecast_qliq_data2', 'forecast_qoil_data1', 'forecast_qoil_data2'
        ]
        stat_objects = self.object.items
        context['statistics'] = stat_objects.values(*group_fields).annotate(**{name: Sum(name) for name in data_fields})
        context['total'] = stat_objects.aggregate(**{name: Sum(name) for name in data_fields})
        return context
