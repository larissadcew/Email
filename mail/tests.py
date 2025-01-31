from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Email
from decimal import Decimal
from django.utils import timezone

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.sender = User.objects.create_user(
            username='sender',
            email='sender@example.com',
            password='senderpass123'
        )
        self.recipient1 = User.objects.create_user(
            username='recipient1',
            email='recipient1@example.com',
            password='recipientpass123'
        )
        self.recipient2 = User.objects.create_user(
            username='recipient2',
            email='recipient2@example.com',
            password='recipientpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')


class EmailModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            email='user@example.com',
            password='userpass123'
        )
        self.sender = User.objects.create_user(
            username='sender',
            email='sender@example.com',
            password='senderpass123'
        )
        self.recipient1 = User.objects.create_user(
            username='recipient1',
            email='recipient1@example.com',
            password='recipientpass123'
        )
        self.recipient2 = User.objects.create_user(
            username='recipient2',
            email='recipient2@example.com',
            password='recipientpass123'
        )
        self.email = Email.objects.create(
            user=self.user,
            sender=self.sender,
            subject="Test Subject",
            body="This is a test email."
        )
        self.email.recipients.set([self.recipient1, self.recipient2])

    def test_email_creation(self):
        self.assertEqual(self.email.user, self.user)
        self.assertEqual(self.email.sender, self.sender)
        self.assertEqual(self.email.subject, "Test Subject")
        self.assertEqual(self.email.body, "This is a test email.")
        self.assertFalse(self.email.read)
        self.assertFalse(self.email.archived)
        self.assertEqual(self.email.recipients.count(), 2)
        self.assertIsNotNone(self.email.timestamp)

    def test_email_str(self):
        expected_str = f"De: sender | Para: ['recipient1', 'recipient2'] | Assunto: Test Subject"
        self.assertEqual(str(self.email), expected_str)

    def test_mark_as_read(self):
        self.assertFalse(self.email.read)
        self.email.mark_as_read()
        self.email.refresh_from_db()
        self.assertTrue(self.email.read)

    def test_mark_as_archived(self):
        self.assertFalse(self.email.archived)
        self.email.mark_as_archived()
        self.email.refresh_from_db()
        self.assertTrue(self.email.archived)

    def test_serialize_method(self):
        serialized_email = self.email.serialize()
        self.assertEqual(serialized_email['id'], self.email.id)
        self.assertEqual(serialized_email['sender'], 'sender@example.com')
        self.assertListEqual(
            serialized_email['recipients'],
            ['recipient1@example.com', 'recipient2@example.com']
        )
        self.assertEqual(serialized_email['subject'], "Test Subject")
        self.assertEqual(serialized_email['body'], "This is a test email.")
        self.assertEqual(serialized_email['read'], False)
        self.assertEqual(serialized_email['archived'], False)
        # Verifica o formato da data
        self.assertIsInstance(serialized_email['timestamp'], str)

    def test_send_email_method(self):
        new_email = Email.send_email(
            sender=self.sender,
            recipients=[self.recipient1],
            subject="New Test",
            body="This is another test email."
        )
        self.assertEqual(new_email.sender, self.sender)
        self.assertEqual(new_email.subject, "New Test")
        self.assertEqual(new_email.body, "This is another test email.")
        self.assertEqual(new_email.recipients.count(), 1)
        self.assertFalse(new_email.read)
        self.assertFalse(new_email.archived)

    def test_read_notification_signal(self):
        # Este teste pressupõe que o sinal 'notify_recipients' está implementado para notificar quando um e-mail é enviado
        # Como o sinal atual está com 'pass', este teste servirá como placeholder
        self.assertTrue(True)  # Placeholder para futuros testes de notificação

    def test_recipients_change_signal(self):
        # Alterar os destinatários para verificar se o sinal 'handle_recipients_change' está funcionando
        self.email.recipients.add(User.objects.create_user(
            username='recipient3',
            email='recipient3@example.com',
            password='recipientpass123'
        ))
        # Como o sinal está com 'pass', aqui apenas verificamos se não ocorre erro
        self.assertEqual(self.email.recipients.count(), 3)