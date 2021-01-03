from django.views import View
from registration.forms import UsersForm
from django.shortcuts import render
from django.http import HttpRequest
from registration.tasks import add_to_email_list
from registration.sub_logger import logger


class HomeView(View):
    def get(self, request):
        assert isinstance(request, HttpRequest)
        logger.info('views.HomeView: GET request')

        return render(
            request, 'home.html'
        )

    def post(self, request):
        assert isinstance(request, HttpRequest)
        logger.info('views.HomeView: POST request')

        usersform = UsersForm(request.POST)

        if usersform.is_valid():
            usersform.save()

            task = add_to_email_list.delay(
                usersform.cleaned_data['username'], usersform.cleaned_data['email']
            )
            logger.info(f'views.HomeView: add_to_email_list task status {task.status}')

        return render(
            request, 'home.html',
            {'form': usersform, 'message': True}
        )
