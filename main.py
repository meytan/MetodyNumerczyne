import integration
import draw_plot, readFile


print("Simpson:")
print(integration.simpson_integration("/home/kacper/repos/MetodyNumerczyne/resources/integration.json"))
print("Monte Carlo:")
print(integration.monte_carlo_integration("/home/kacper/repos/MetodyNumerczyne/resources/integration.json"))

