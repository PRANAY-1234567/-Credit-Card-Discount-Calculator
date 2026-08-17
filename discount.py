#wap to give 10% off only who is
# purchasing in credit card and min 3 product should
# purchase and each product price should be more than 500

mode=eval(input("enter the Payment--mode "))
if mode=="credit-card":
    product=eval(input("enter the Product Number"))
    if product>=3:
        P1=eval(input("enter the Price"))
        P2=eval(input("enter the Price"))
        P3=eval(input("enter the Price"))
        if P1>=500 and P2>=500 and P3>=500:
            total=(P1+P2+P3)
            price=total-(total*0.10)
            print(f'Total amount is {total} and discount amount is'
                  f'{price}')
        else:
            print("Product price is less than 500")

    else:
        print("less than 3 Product")

else:
    print("Cash----->💷")
