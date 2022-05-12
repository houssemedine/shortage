from django.test import TestCase
from shortage.models import Core

# models test
class CoreTest(TestCase):

    def create_core(self, material="",
                            division="At recusandae Do earum enim",
                            program="Nesciunt molestias nisi quo p",
                            supplier="Voluptas odit accusamus cupidi",
                            part_number	="947",
                            type_of_alert ="Elit quis voluptatem Volupta",
                            requested_date="1985-12-03 01:00:00+01",
                            needed_quantity="705",
                            subject="Nisi voluptatem vol",
                            status="Stand by",
                            closing_date='1985-12-03 01:00:00+01',
                            duration_of_the_event="Laborum asperiores optio ea d",
                            created_on="1985-12-03 01:00:00+01",
                            updated_on="1985-12-03 01:00:00+01",
                            created_by="1"
                    ):
        return Core.objects.create(material=material,
                                    division=division,
                                    program=program,
                                    supplier=supplier,
                                    part_number=part_number,
                                    type_of_alert=type_of_alert,
                                    requested_date=requested_date,
                                    needed_quantity=needed_quantity,
                                    subject=subject,
                                    status=status,
                                    closing_date=closing_date,
                                    duration_of_the_event=duration_of_the_event,
                                    created_on=created_on,
                                    updated_on=updated_on,
                                    created_by=created_by
                                    )

    def test_core_creation(self):
        w = self.create_core()
        self.assertTrue(isinstance(w, Core))
        self.assertEqual(w.__unicode__(), w.material)