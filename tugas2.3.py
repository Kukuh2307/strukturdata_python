def balikSetiapKata(kalimat):
  covnerToSplit = kalimat.split()
  covnerToSplit.reverse()
  print(kalimat)
  print(" ".join(covnerToSplit))

kata = "Ini Ibu Budi"
balikSetiapKata(kata)