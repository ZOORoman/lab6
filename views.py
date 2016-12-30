class BookView(View):
    def get(self, request):
        a = BookViewModel.objects.all()
        return render(request, 'order.html', {'a':a})
