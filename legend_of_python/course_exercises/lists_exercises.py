# Lego 🎁

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

print(min(lego_parts))
print(max(lego_parts))

# Reading List 📕📘

reading_list = ["Harry Potter", "1984", "The Fault in Our Stars", "The Mom Test", "Life in Code"]

reading_list.append("Pachinko")
reading_list.remove("1984")
reading_list.pop(1)
print(reading_list)

# Playlist 💽

playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]

for i in playlist:
  print(i)

for i in range(len(playlist)):

  print(playlist[i])
