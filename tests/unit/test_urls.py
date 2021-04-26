from django.contrib.auth import get_user_model
from django.urls import reverse
from pytest import fixture, mark


@fixture
def index_list_templates():
    return [
        "base.html",
        "pages/index.html",
    ]


@mark.django_db
@mark.parametrize(
    "url, status",
    [("", 200), (reverse("pages:frontpage"), 200)],
)
def test_route_anon_index_urls(client_anon, url, status, index_list_templates):
    """URL access for visitor and checks templates."""
    response = client_anon.get(url)

    assert response.status_code == status
    for template in index_list_templates:
        assert template in [t.name for t in response.templates]


@mark.django_db
def test_route_anon_about(client_anon):
    response = client_anon.get(reverse("pages:about"))

    for template in [
        "base.html",
        "pages/about.html",
    ]:
        assert template in [t.name for t in response.templates]


@mark.django_db
def test_route_logged_dashboard(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(
        username=username, password=password
    )
    # Use this:
    client.force_login(user)
    # Or this:
    client.login(username=username, password=password)
    response = client.get(reverse("pages:dashboard"))

    for template in [
        "base.html",
        "pages/dashboard.html",
    ]:
        assert template in [t.name for t in response.templates]
