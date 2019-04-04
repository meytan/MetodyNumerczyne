from draw_plot import draw_plot
from interpolation import newton_interpolation
from readFile import read_json
from system_of_equation import system_of_equation_cramer
from non_linear_equation import bisection, fun, nm_method
#draw_plot(newton_interpolation, [-2, 4])

# x = system_of_equation_cramer([[2., 5., 3., 5.], [4., 2., 5., 4.], [3., 8., 4., 9.]])

draw_plot(fun)

x = nm_method()
print(x)

x = bisection()
print(x)


print(x)


