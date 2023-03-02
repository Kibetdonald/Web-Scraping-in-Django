from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bs4 import BeautifulSoup
from .models import Course
from .serialize import CourseSerializer
import requests
from django.http import HttpResponse

def scrape_courses(request):
    url = 'https://www.classcentral.com/subjects'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    courses = soup.find_all('div', {'class': 'search-card'})

    for course in courses:
        title = course.find('div', {'class': 'text-block'}).h3.text
        description = course.find('div', {'class': 'text-block'}).p.text
        url = 'https://www.classcentral.com' + course.find('a', {'class': 'color-charcoal'})['href']
        image_url = course.find('div', {'class': 'background-image'})['style'][23:-3]

        Course.objects.create(title=title, description=description, url=url, image_url=image_url)

    return HttpResponse('Courses scraped and saved to database!')


class CoursesList(APIView):
    def get(self, request):
        courses = Course.objects.all()
        dlSerializeObj = CourseSerializer(
            courses, many=True)
        return Response(dlSerializeObj.data)
