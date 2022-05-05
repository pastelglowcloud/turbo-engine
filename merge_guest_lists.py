def combine_guests(guests1, guests2):
  combined_dict = {}
  for guest in guests1:
    if guest not in combined_dict:
      combined_dict[guest] = guests1[guest]
  for guest in guests2:
    if guest not in combined_dict:
      combined_dict[guest] = guests2[guest]
  return combined_dict