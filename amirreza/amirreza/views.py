from django.shortcuts import render


people = {
    111: {"name": "Amirreza", "age": 11, "city": "Tehran"},
    123: {"name": "Mohammad", "age": 29, "city": "Qom"}
}
def amirreza_handler(request, pk):
    return render(
        request=request,
        template_name='amirreza/index.html',
        context=people.get(pk)
    )

