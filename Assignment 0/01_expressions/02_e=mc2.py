from rich.console import Console

console = Console()

Constant_Speed_Light = 299792458

def mass_energy_equivalence(mass_value:float)->float:
  energy_value = mass_value * Constant_Speed_Light**2
  return energy_value


def main():

  console = Console()
  mass = float(input("Enter the mass of an object: "))
  energy = mass_energy_equivalence(mass)

  console.print(f"E = M x C^2",style="bold yellow")
  console.print(f"m = {mass}" , style="bold green ")
  console.print(f"E = {energy} joule" , style="bold white on blue")


if __name__ == "__main__":
  main()