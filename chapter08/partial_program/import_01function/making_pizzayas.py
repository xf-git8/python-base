def make_pizza(size,*toppings):
    """
    #定义一个制作pizzas的函数
    :param size:
    :param toppings: * 打包参数到元组中，函数定义时不确定传入的参数有多使用
    :return:
    """
    print(f"making a {size}-inch pizza with the follow toppings")
    for topping in toppings:
        print(f"-{topping}")
pizza = make_pizza(16,"peperoni")
pizzas= make_pizza(12,"mushrooms","green peppers","extra cheese")
