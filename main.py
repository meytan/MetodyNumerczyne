from draw_plot import draw_plot
from interpolation import newton_interpolation
from system_of_equation import system_of_equation_cramer

#draw_plot(newton_interpolation, [-2, 4])

x = system_of_equation_cramer([[2., 5., 3., 5.], [4., 2., 5., 4.], [3., 8., 4., 9.]])

print(x)



