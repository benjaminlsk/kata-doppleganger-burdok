from mail_sender import MailSender, Request
class MailSender:
    base_url = "https://api.mailsender.com"

    def __init__(self, http_client):
        self.http_client = http_client

    def send_v1(self, user, message):
        # Corrigé ! Doit être `Request(user.name, user.email, ...)`
        request = Request(user.name, user.email, "New notification", message)
        return self.http_client.post(self.base_url, request)

class MockUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class MockHttpClient:
    def __init__(self):
        self.post_called = False
        self.post_args = None

    def post(self, url, request):
        self.post_called = True
        self.post_args = (url, request)

def test_send_v1():
    # Créer une instance de MockHttpClient
    http_client = MockHttpClient()

    # Créer une instance de MockUser
    user = MockUser("Test User", "test@example.com")

    # Créer une instance de MailSender avec MockHttpClient
    mail_sender = MailSender(http_client)

    # Appeler la méthode send_v1
    mail_sender.send_v1(user, "Test message")

    # Vérifier que la méthode post de MockHttpClient a été appelée avec les bons arguments
    assert http_client.post_called
    assert http_client.post_args == (
        MailSender.base_url,
        Request(user.email, user.name, "New notification", "Test message")
    )

def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    pass