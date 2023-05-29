# Importing Required Modules
from rembg import remove
from PIL import Image

# Store path of the image in the variable input_path
input_path = r'C:\Users\goura\OneDrive\Desktop\Gourav Kumar\Projects\Virtual threads\Frontend\Web\Shirts\Tank top.png'

# Store path of the output image in the variable output_path
output_path = r'C:\Users\goura\OneDrive\Desktop\Gourav Kumar\Projects\Virtual threads\Frontend\Web\Shirts\Tank top.png'

# Processing the image
input = Image.open(input_path)

#input = remove(input)
width, height = input.size
 
newsize = (400, 581)
output = input.resize(newsize)
output.show() 

#Saving the image in the given path
output.save(output_path)


