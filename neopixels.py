import sys
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 100

ORDER = neopixel.GRB

# Initialize
pixels = neopixel.NeoPixel(
  pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

print("Neopixels initialized!", file=sys.stderr)

# Blacks out all pixels
def noir():
  print("Running noir", file=sys.stderr)
  pixels.fill((0, 0, 0))
  pixels.show()

def rain():
  print("Running rain", file=sys.stderr)
  for j in range(255):
    for i in range(num_pixels):
      pixel_index = (i * 256 // num_pixels) + j
      pixels[i] = wheel(pixel_index & 255)
    pixels.show()
    time.sleep(.025)

def green():
  print("Running green", file=sys.stderr)
  pixels[0] = (0, 0, 0)
  for i in range(num_pixels):
      pixels[i] = (255, 0, 0)
      pixels[i - 1] = (128, 0, 0)
      time.sleep(0.2)
      pixels.show()

def pink():
  print("Running pink", file=sys.stderr)
  pixels[0] = (0, 0, 0)
  for i in range(num_pixels):
      pixels[i] = (105, 255, 180)
      pixels[i - 1] = (52, 128, 90)
      time.sleep(0.2)
      pixels.show()

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


#while True:
#    rainbow_cycle(0.025)  # rainbow cycle with delay per step
