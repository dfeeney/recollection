import logging

from django.core.management.base import NoArgsCommand

from freemix.dataset.models import DataSourceTransaction


class Command(NoArgsCommand):
    help = ("Delete DataSourceTransaction records that have a modified "
            " date older than the expiration time")

    def handle_noargs(self, **options):
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        logging.debug("Deleting expired "
                      "freemix.dataset.models.DataSourceTransaction models")
        transactions = DataSourceTransaction.objects.all()
        expired_transactions = [x for x in transactions if x.is_expired()]
        record_count = len(expired_transactions)
        for expired in expired_transactions:
            expired.delete()
        logging.debug(
            "Deleted %s DataSourceTransaction records" % record_count)
