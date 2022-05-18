from __future__ import division
from django.test import TestCase
from shortage.models import Core,ZPP_MD_Stock

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

class ZppTest(TestCase):

    def create_zpp(self,year='2022',
                        week='12',
                        division='2110',
                        material='IS0059541H',
                        plan_date='2022-02-03 01:00:00+01',
                        mrp_element='',
                        data_for_planning_element	='',
                        action_message	='',
                        Input_need=0.000,
                        available_quantity=0.000,
                        reorder_date='2022-02-03 01:00:00+01'	,
                        vendor	='',
                        customer=''	,
                        uploaded_at="1985-12-03 01:00:00+01",
                        uploaded_by="1"

                    ):
        return ZPP_MD_Stock.objects.create(year=year,
                                            week=week,
                                            division=division,
                                            material=material,
                                            plan_date=plan_date,
                                            mrp_element=mrp_element,
                                            data_for_planning_element	=data_for_planning_element,
                                            action_message	=action_message,
                                            Input_need=Input_need,
                                            available_quantity=available_quantity,
                                            reorder_date=reorder_date,
                                            vendor	=vendor,
                                            customer=customer	,
                                            uploaded_at=uploaded_at,
                                            uploaded_by=uploaded_by
                                            )

    def test_zpp_creation(self):
        w = self.create_zpp()
        self.assertTrue(isinstance(w, ZPP_MD_Stock))
        self.assertEqual(w.__unicode__(), w.material)