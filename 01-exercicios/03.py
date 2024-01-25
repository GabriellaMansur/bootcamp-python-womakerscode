quilometros = float(input("Digite uma quantidade de quilômetros para serem convertidos: "))
centimetros = quilometros * 100000
milimetros = quilometros * 1000000

print(f"{quilometros:.2f} km equivalem a {centimetros:.2f} centímetros")
print(f"{quilometros:.2f} km equivalem a {milimetros:.2f} milímetros")