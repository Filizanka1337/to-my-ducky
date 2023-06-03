import ctypes

# Wywołanie funkcji msgbox z biblioteki ctypes
ctypes.windll.user32.MessageBoxW(0, "hi", "Message", 1)

