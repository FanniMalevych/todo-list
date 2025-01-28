from django.urls import path

from tasks.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    # # path("formats", formats_view, name="formats")
    # path("formats", FormatsView.as_view(), name="formats"),
    # path("formats/create", FormatsCreateView.as_view(), name="format-create"),
    # path("formats/<int:pk>/update", FormatsUpdateView.as_view(), name="format-update"),
    # path("books", BookListView.as_view(), name="books"),
    # path("books/<int:pk>", book_detail_view, name="book-detail"),
    # path("books/<int:pk>/update", BookUpdateView.as_view(), name="book-update"),
    # path("book/create", BookCreateView.as_view(), name="book-create"),
    # path("author/create", AuthorCreateView.as_view(), name="author-create"),
    # path("test", TestListView.as_view(), name="test-list"),
    # # path("test/create", test_create_view, name="test-create")
]

app_name = 'tasks'