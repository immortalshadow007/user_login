from django.apps import AppConfig
import logging as log

logger = log.getLogger(__name__)

class UserloginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userlogin'

    # Any startup tasks for the mobile_number app can be included here
    def ready(self):
        logger.info("UserLogin App is ready.")