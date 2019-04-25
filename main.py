from draw_plot import draw_plot
from interpolation import newton_interpolation
from readFile import read_json, read_json_sys
from system_of_equation import system_of_equation_cramer, system_of_equation_gauss
from non_linear_equation import bisection, fun, nm_method
#draw_plot(newton_interpolation, [-2, 4])

# x = system_of_equation_cramer([[2., 5., 3., 5.], [4., 2., 5., 4.], [3., 8., 4., 9.]])


o = read_json_sys()
result = system_of_equation_gauss(o)
print(result)


