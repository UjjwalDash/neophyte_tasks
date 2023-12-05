
#Click key g -> grouping"
#click key s -> Saving coordinates in output.txt


import cv2

coordinates=[]
subcoord=[]
# Function to get mouse click coordinates
def get_coordinates(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        subcoord.append([x,y])
        cv2.putText(image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        print(subcoord)
        print(f"Coordinates: ({x}, {y})")

# Read an image
image = cv2.imread('superheros.jpg')

# Create a window and set the callback function
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', get_coordinates)

while True:
    # Display the image
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF
    # Break the loop if 'Esc' key is pressed
    if key == 27:
        break
    if key==ord('g'):
        coordinates.append(subcoord)
        subcoord=[]
        print("All coordinates\n",coordinates)
    if key == ord('s'):
        fname='output.txt'
        with open(fname,'w') as file:
            file.write(str(coordinates))
        print("File saved")
            

# Release resources
cv2.destroyAllWindows()

