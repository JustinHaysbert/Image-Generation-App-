import customtkinter as ctk
import tkinter
import os
from openai import OpenAI
import openai
from PIL import Image, ImageTk
import requests, io

def generate():
    openai.api_key = os.getenv('OPENAI_API_KEY')

    
    

    response = openai.images.generate(
        model = "dall-e-3",
        ##gets promt from tkinter entry
        prompt = prompt_entry.get("0.0",tkinter.END),
        size = "1024x1024",
        ##gets style from tkinter selection
        style = style_dropdown.get(),
        quality = quality_dropdown.get(),
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)
    ##Gets the generated image from the URL openai provides
    response = requests.get(image_url)
    #read bytes of image and open
    image = Image.open(io.BytesIO(response.content))
    #creates the tkinter image
    image = ImageTk.PhotoImage(image)

    #puts the tkinter image on the canvas
    canvas.image = image
    canvas.create_image (0,0, anchor="nw", image=image)

## Establishes the root CTk
root = ctk.CTk()
root.title("AI Image Generator")

## Creates a frame for our project that lies within the root
input_frame = ctk.CTkFrame(root)
## use pack to make the frame show in Tkinter
input_frame.pack(side='left', expand=True, padx=20, pady=20)

## Creating the Prompt label and setting it inside of our input frame
prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
## Here I use grid to place a grid like section of labels, I want the prompt label at index 0
prompt_label.grid(row=0, column=0, padx = 10, pady = 10)

## Creating our textbox so user can input
prompt_entry = ctk.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row= 0, column =1, padx = 10, pady = 10)

#new label for style option
style_label = ctk.CTkLabel(input_frame, text="Style")
style_label.grid(row=1, column=0, padx = 10, pady=10)

## dropdown option for the style label with options vivid and natural
style_dropdown = ctk.CTkComboBox(input_frame, values = ["vivid", "natural"])
style_dropdown.grid(row=1, column = 1, padx=10, pady=10)

##label for the number of images you want generated 
#number_label = ctk.CTkLabel(input_frame, text = "# of Images")
#number_label.grid(row=2, column = 0)

## creates a slider option for user to pick from 1-10 images generated
#number_slider = ctk.CTkSlider(input_frame, from_ =1, to=10, number_of_steps=9)
#number_slider.grid(row=2, column=1)

quality_label = ctk.CTkLabel(input_frame, text = "Quality")
quality_label.grid(row=2, column=0)

quality_dropdown = ctk.CTkComboBox(input_frame, values = ["standard", "hd"])
quality_dropdown.grid(row=2, column=1, padx = 10, pady = 10)

## this creates a button for the user to generate their image
generate_button = ctk.CTkButton(input_frame, text="Generate", command = generate)
#Grid the button in and make it span 2 columns, sticky news makes our button wider in all directions
generate_button.grid(row=3, column=0, columnspan = 2, sticky = "news", padx=10, pady=10)

## this created our blank canvas to put our generated image
canvas = tkinter.Canvas(root, width=1024, height=1024)
canvas.pack(side = "left")

root.mainloop()