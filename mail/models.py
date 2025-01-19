# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.validators import EmailValidator


class User(AbstractUser):
    """
    Modelo de Usuário personalizado que estende o AbstractUser do Django.
    """
    # Caso deseje adicionar campos personalizados no futuro, pode fazê-lo aqui.
    
    def __str__(self):
        return self.username


class Email(models.Model):
    """
    Modelo que representa um e-mail enviado entre usuários.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="emails",
        help_text="Usuário proprietário da caixa de entrada."
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="emails_sent",
        help_text="Usuário que enviou o e-mail."
    )
    recipients = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="emails_received",
        help_text="Usuários que recebem o e-mail."
    )
    subject = models.CharField(
        max_length=255,
        help_text="Assunto do e-mail."
    )
    body = models.TextField(
        blank=True,
        help_text="Corpo do e-mail."
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Data e hora em que o e-mail foi enviado."
    )
    read = models.BooleanField(
        default=False,
        help_text="Indica se o e-mail foi lido."
    )
    archived = models.BooleanField(
        default=False,
        help_text="Indica se o e-mail foi arquivado."
    )

    def __str__(self):
        return f"De: {self.sender.username} | Para: {[user.username for user in self.recipients.all()]} | Assunto: {self.subject}"

    def mark_as_read(self):
        """
        Marca o e-mail como lido.
        """
        if not self.read:
            self.read = True
            self.save()

    def mark_as_archived(self):
        """
        Marca o e-mail como arquivado.
        """
        if not self.archived:
            self.archived = True
            self.save()

    def serialize(self):
        """
        Serializa o objeto de e-mail para um formato compatível com JSON.
        """
        return {
            "id": self.id,
            "sender": self.sender.email,
            "recipients": [user.email for user in self.recipients.all()],
            "subject": self.subject,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "read": self.read,
            "archived": self.archived
        }

    @classmethod
    def send_email(cls, sender, recipients, subject, body):
        """
        Método de classe para enviar um e-mail.
        
        Parâmetros:
        - sender: Instância de User que está enviando o e-mail.
        - recipients: Lista de instâncias de User que receberão o e-mail.
        - subject: Assunto do e-mail.
        - body: Corpo do e-mail.
        
        Retorna:
        - Instância de Email criada.
        """
        email = cls.objects.create(
            user=sender,  # Supondo que 'user' é o dono da caixa de entrada, pode ser ajustado conforme a lógica da aplicação
            sender=sender,
            subject=subject,
            body=body
        )
        email.recipients.set(recipients)
        return email


# Sinais para Atualizar Campos Automáticos ou Realizar Ações Extras
@receiver(post_save, sender=Email)
def notify_recipients(sender, instance, created, **kwargs):
    """
    Sinal para notificar os destinatários quando um novo e-mail é enviado.
    """
    if created:
        # Aqui você pode adicionar lógica para notificar os destinatários, como enviar uma notificação
        # Por exemplo: enviar um e-mail real, criar uma notificação no aplicativo, etc.
        pass  # Placeholder para lógica de notificação


@receiver(m2m_changed, sender=Email.recipients.through)
def handle_recipients_change(sender, instance, action, **kwargs):
    """
    Sinal para lidar com alterações na lista de destinatários.
    """
    if action == "post_add":
        # Por exemplo, enviar notificações adicionais após adicionar novos recipientes
        pass  # Placeholder para lógica adicional