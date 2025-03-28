from typing import Any
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2OpError
import time

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("checking db availability.......")
        db_up = False

        while db_up is False:
            try:
                self.check(databases = ['default'])
                db_up = True
                
            except(Psycopg2OpError,OperationalError):
                self.stdout.write("waiting for 1 sec to start the db ...")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("db srarted!..."))

        
        
