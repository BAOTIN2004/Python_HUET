from sympy import*
from sympy.plotting import plot
def ham_so():
    x=symbols('x')
    f=x**4-2*x**2-3
    return f

def dao_ham_cap_1():
    x=symbols('x')
    f=diff(ham_so(),x)
    return f

def dao_ham_cap_2():
    x=symbols('x')
    f=diff(dao_ham_cap_1(),x)
    return f

def dao_ham_cap_3():
    x=symbols('x')
    f=diff(dao_ham_cap_2(),x)
    return f

def main():
    x=symbols('x')
    y=ham_so()
    y1=dao_ham_cap_1()
    y2=dao_ham_cap_2()
    y3=dao_ham_cap_3()
    do_thi=plot(y,y1,y2,y3,(x,-10,10,10000),xlabel='Trục x',ylabel=' Trục y',legend=True,show=False)
    do_thi.show()
if __name__=="__main__":
    main()