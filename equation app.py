import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Définir les bornes de x
x = np.linspace(-20, 20, 400)

# Résolution des équations pour y
y1 = 12 - 2 * x
y2 = (74 - 5 * x) / 8
y3 = (24 - x) / 6

# Configuration du layout de Streamlit
st.title("Représentation graphique des inéquations")

st.write("""
    Ce graphique montre la solution du système d'inéquations suivant :
    - \( 2x + y \geq 12 \)
    - \( 5x + 8y \geq 74 \)
    - \( x + 6y \geq 24 \)
""")

# Tracer les droites des équations
fig, ax = plt.subplots(figsize=(8, 6))

# Tracer les lignes correspondant aux égalités
ax.plot(x, y1, label=r'$2x + y = 12$', color='blue')
ax.plot(x, y2, label=r'$5x + 8y = 74$', color='red')
ax.plot(x, y3, label=r'$x + 6y = 24$', color='green')

# Remplir les zones correspondant aux inéquations
ax.fill_between(x, y1, 50, where=(y1 >= 50), color='blue', alpha=0.2)  # y >= 12 - 2x
ax.fill_between(x, y2, 100, where=(y2 >= 100), color='red', alpha=0.2)  # y >= (74 - 5x) / 8
ax.fill_between(x, y3, 100, where=(y3 >= 100), color='green', alpha=0.2)  # y >= (24 - x) / 6

# Personnaliser l'apparence du graphique
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title('Représentation des inéquations')

# Ajouter une légende
ax.legend(loc='best')

# Affichage du graphique
st.pyplot(fig)
