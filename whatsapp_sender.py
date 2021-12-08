import pywhatkit
# import Image

# pywhatkit.sendwhats_image("+918527399784", "GDSC VIT Leads.png", "Here is the image", 10, True, 5)
# pywhatkit.sendwhatmsg_instantly('+918527399784','This message is sent using Python',wait_time=10)
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+919819910060",
                        "Hello, this message is sent from python",
                        14, 2)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")
