from celery import shared_task
from cars.models import Car
from dealers.models import DealerCar, DealerProfile, TransactionToShowroom
from showrooms.models import ShowroomProfile, ShowroomCar, TransactionToCustomer
from customers.models import CustomerProfile, CustomerCar
from django.db import transaction
from django.db.models import Q
from sales.models import DealerSales, ShowroomSales


@shared_task
def buy_car_from_dealer():
    # create QuerySet all showrooms
    for showroom_item in ShowroomProfile.objects.all():
        # create query showroom
        query = showroom_item.showroom_query

        # select 2 fields from query instance (dictionary)
        # we can select all fields
        query_make = query.get("make")
        query_model = query.get("model")
        query_price = query.get("price")

        # check what is happened!
        with open('cars.txt', 'a') as f:
            f.write(f'1_showroom: - query_make:{query_make}, -query model {query_model} -sh_item: {showroom_item},'
                    f'price_type:{type(query_price)} \n')

        # creating QuerySet that matches the showroom's query
        dealer_cars = DealerCar.objects.filter(
            (Q(car__make__iexact=query_make) |
             Q(car__model__iexact=query_model)) &
            Q(price__lte=query_price)
        )

        for d_car in dealer_cars:
            # select price
            dealer_price = d_car.price

            if DealerSales.objects.filter(car__pk=d_car.car.pk).exists():
                item = DealerSales.objects.get(car__pk=d_car.car.pk)
                if item.is_active:
                    dealer_price = dealer_price - (item.discount * dealer_price)
                    print(f'dealer_price {dealer_price}')

            # check what is happened!
            with open('cars.txt', 'a') as f:
                f.write(f'2_dealer: - dealer_car_inst{d_car} - price {dealer_price} - car_count: {d_car.count} \n')

            # if not cars then scip
            if d_car.count == 0:
                continue

            # if money is not enough
            if showroom_item.balance < dealer_price:
                continue

            # # if count of cars = 0
            # if d_car.count <= 0:
            #     continue

            # check what is happened!
            with open('cars.txt', 'a') as f:
                f.write(f'3_dealer: - car_inst:{d_car} - car_count:{d_car.count} - car_price:{dealer_price} \n')

            # instances for recording to DB
            showroom_car = Car.objects.get(pk=d_car.car.pk)
            # showroom_profile = ShowroomProfile.objects.get(pk=showroom_item.pk)
            dealer_profile = DealerProfile.objects.get(pk=d_car.dealer.pk)

            with transaction.atomic():
                # add car to showroom, increase count
                result = ShowroomCar.objects.update_or_create(
                    car=showroom_car,
                    showroom=showroom_item,
                    dealer=dealer_profile,
                    # price=dealer_price


                )
                if result[1]:
                    result[0].price = dealer_price + ((dealer_price * 30) / 100)
                    result[0].save()
                # if result == False (item already exist), then increase count +1

                if not result[1]:
                    result[0].price = dealer_price + ((dealer_price * 30) / 100)  # increase price before selling
                    result[0].count += 1
                    result[0].is_active = True
                    result[0].save()

                # decrease balance in showroom
                showroom_item.balance -= dealer_price
                showroom_item.save()

                # increase balance in dealer
                dealer_profile.balance += dealer_price
                dealer_profile.save()

                # decrease car in dealer car
                d_car.count -= 1
                # if cars instance == 0, is active == False
                if d_car.count == 0:
                    d_car.is_active = False
                d_car.save()

                # add transactions
                TransactionToShowroom.objects.create(
                    car=showroom_car,
                    showroom=showroom_item,
                    dealer=dealer_profile,
                    price=dealer_price,
                    count=1,
                )


@shared_task
def buy_car_from_showroom():
    # create QuerySet all customer
    for customer_item in CustomerProfile.objects.all():
        # create query showroom
        query = customer_item.customer_query

        # select 2 fields from query instance (dictionary)
        # we can select all fields
        query_make = query.get("make")
        query_model = query.get("model")

        # check what is happened!
        with open('cars.txt', 'a') as f:
            f.write(f'41_showroom-{query_make} - {query_model}  -{customer_item.pk}-\n')

        # creating QuerySet that matches the showroom's query
        showroom_car = ShowroomCar.objects.filter(
            Q(car__make__iexact=query_make) |
            Q(car__model__iexact=query_model)

        )
        for sh_car in showroom_car:
            # select price
            showroom_price = sh_car.price

            if sh_car.count == 0:
                continue

            # if money is not enough
            if customer_item.balance < showroom_price:
                continue

            # check what is happened!
            with open('cars.txt', 'a') as f:
                f.write(f'42_dealer{sh_car} - {showroom_price} \n')

            # instances for recording to DB
            customer_car = Car.objects.get(pk=sh_car.car.pk)
            # showroom_profile = ShowroomProfile.objects.get(pk=showroom_item.pk)
            showroom_profile = ShowroomProfile.objects.get(pk=sh_car.showroom.pk)

            with transaction.atomic():
                # add car to showroom, increase count
                result = CustomerCar.objects.update_or_create(
                    car=customer_car,
                    customer=customer_item,
                    showroom=showroom_profile,
                    price=showroom_price

                )
                # if result == False (item already exist), then increase count +1
                if not result[1]:
                    result[0].count += 1
                    result[0].is_active = True
                    result[0].save()

                # decrease balance in customer
                customer_item.balance -= showroom_price
                customer_item.save()

                # increase balance in showroom
                showroom_profile.balance += showroom_price
                showroom_profile.save()

                # decrease car in customer car
                sh_car.count -= 1
                # if cars instance == 0, is active == False
                if sh_car.count == 0:
                    sh_car.is_active = False
                sh_car.save()

                # add transactions
                TransactionToCustomer.objects.create(
                    car=customer_car,
                    customer=customer_item,
                    showroom=showroom_profile,
                    price=showroom_price,
                    count=1,

                )
