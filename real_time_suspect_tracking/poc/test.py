import face_recognition
from PIL import Image, ImageDraw


known_image = face_recognition.load_image_file("test.jpg")
unknown_image = face_recognition.load_image_file("test2.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)


#image = face_recognition.load_image_file("test4.jpg")
#face_locations = face_recognition.face_locations(image)
#print(face_locations)


# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("test4.jpg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    #See if the face is a match for the known face(s)
    #matches = face_recognition.compare_faces(face_encoding, face_encoding)

    name = "Unknown"

    #If a match was found in known_face_encodings, just use the first one.
    #if True in matches:
        #first_match_index = matches.index(True)
        #name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
pil_image.save("detection.jpg")
